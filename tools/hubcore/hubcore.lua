-- HubCore HBK4-03: an executable, bounded K4 interpretation of 1-3-4-6.
-- Original REIK/TCGE kernel is not imported, replaced, or modified.
-- Three Boolean selectors are distinct from the canonical 0/U/1 vocabulary.
local HubCore = {
  system = "MonadMetatronSystem",
  config = {units = 1, bits = 3, nodes = 4, pairs = 6},
  vertices = {
    {name="N", xyz={1,1,1}},
    {name="E", xyz={1,-1,-1}},
    {name="S", xyz={-1,1,-1}},
    {name="W", xyz={-1,-1,1}}
  },
  matchings = {
    {{"N","E"},{"S","W"}},
    {{"N","S"},{"E","W"}},
    {{"N","W"},{"E","S"}}
  }
}

local function fail(message) error("HubCore validation: " .. message, 2) end
local function edge_key(a,b)
  if a > b then a,b = b,a end
  return a .. "-" .. b
end

function HubCore.initialize()
  local c=HubCore.config
  if c.units~=1 or c.bits~=3 or c.nodes~=4 or c.pairs~=6 then
    fail("expected 1 unit, 3 bits, 4 nodes, 6 pairs")
  end
  if #HubCore.vertices~=c.nodes or #HubCore.matchings~=c.bits then
    fail("vertex or matching count mismatch")
  end
  local names={}
  for _,v in ipairs(HubCore.vertices) do
    if names[v.name] or #v.xyz~=3 then fail("invalid vertex") end
    names[v.name]=true
  end
  local all_edges={}
  for _,matching in ipairs(HubCore.matchings) do
    if #matching~=2 then fail("a matching must have two pairs") end
    local seen={}
    for _,edge in ipairs(matching) do
      local a,b=edge[1],edge[2]
      if not names[a] or not names[b] or a==b or seen[a] or seen[b] then
        fail("matching must touch each vertex exactly once")
      end
      seen[a]=true; seen[b]=true
      local key=edge_key(a,b)
      if all_edges[key] then fail("pair repeated across matchings") end
      all_edges[key]=true
    end
  end
  local count=0
  for _ in pairs(all_edges) do count=count+1 end
  if count~=c.pairs then fail("expected six unique pairs") end
  for i=1,c.nodes do
    for j=i+1,c.nodes do
      local p,q=HubCore.vertices[i].xyz,HubCore.vertices[j].xyz
      local d=0
      for k=1,3 do d=d+(p[k]-q[k])^2 end
      if d~=8 then fail("non-regular tetrahedron coordinates") end
    end
  end
  return c
end

function HubCore.state(number)
  if type(number)~="number" or number%1~=0 or number<0 or number>7 then
    fail("state must be an integer from 0 through 7")
  end
  local bits={}; local edges={}; local degree={N=0,E=0,S=0,W=0}
  for i=1,3 do
    local b=math.floor(number/2^(3-i))%2
    bits[i]=b
    if b==1 then
      for _,edge in ipairs(HubCore.matchings[i]) do
        edges[#edges+1]={edge[1],edge[2]}
        degree[edge[1]]=degree[edge[1]]+1
        degree[edge[2]]=degree[edge[2]]+1
      end
    end
  end
  local expected=bits[1]+bits[2]+bits[3]
  for _,d in pairs(degree) do
    if d~=expected then fail("mapped graph must be regular") end
  end
  return {code=table.concat(bits),edges=edges,edge_count=#edges,degree=expected}
end

local function quote(s) return '"' .. s .. '"' end -- fixed literal identifiers only
function HubCore.coordinate_json()
  HubCore.initialize()
  local c=HubCore.config
  local output={
    '{',
    '"schema":"hubcore-k4-v1",',
    '"system":'..quote(HubCore.system)..',',
    '"config":{"units":'..c.units..',"bits":'..c.bits..',"nodes":'..c.nodes..',"pairs":'..c.pairs..'},',
    '"bit_semantics":"three independent Boolean switches, not three-valued digits",',
    '"monad":{"is_graph_vertex":false,"xyz":[0,0,0]},',
    '"coordinate_claim":"constructed exact 3D embedding; not measured from generated art",',
    '"vertices":['
  }
  for i,v in ipairs(HubCore.vertices) do
    if i>1 then output[#output+1]=',' end
    output[#output+1]='{"id":'..quote(v.name)..',"xyz":['..table.concat(v.xyz,',')..']}'
  end
  output[#output+1]='],"matchings":['
  for i,m in ipairs(HubCore.matchings) do
    if i>1 then output[#output+1]=',' end
    local parts={}
    for _,e in ipairs(m) do
      parts[#parts+1]='['..quote(e[1])..','..quote(e[2])..']'
    end
    output[#output+1]='['..table.concat(parts,',')..']'
  end
  output[#output+1]='],"states":['
  for n=0,7 do
    if n>0 then output[#output+1]=',' end
    local s=HubCore.state(n); local parts={}
    for _,e in ipairs(s.edges) do
      parts[#parts+1]='['..quote(e[1])..','..quote(e[2])..']'
    end
    output[#output+1]='{"bits":'..quote(s.code)..',"edges":['..table.concat(parts,',')..'],"edge_count":'..s.edge_count..',"degree":'..s.degree..'}'
  end
  output[#output+1]='],"reik_status":"0 HOLD","external_echo":false}'
  return table.concat(output)
end

-- texlua tools/hubcore/hubcore.lua prints the generated map in JSON.
-- dofile("tools/hubcore/hubcore.lua") returns the module for reuse.
if arg and arg[0] and arg[0]:match("hubcore%.lua$") then
  io.write(HubCore.coordinate_json(),"\n")
end
return HubCore
