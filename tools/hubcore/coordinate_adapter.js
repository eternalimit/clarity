'use strict';
// HBK4-04: opt-in local consumer, NOT a deployed Cosmos7/Clarity Trunk integration.
// No mutation of REIK_ROOT.md, kernel001.py, or REIK/TCGE evidence state.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const PIN = '031e6fa2af07a35c9ac48153a65c5c5e9090c36aa54a1816c54592b9b9cc092c';
const DEFAULT_PATH = path.resolve(__dirname, '../../research/hubcore/HBK4-03/coordinate_mapping.json');
const coords = {N:[1,1,1], E:[1,-1,-1], S:[-1,1,-1], W:[-1,-1,1]};
const matchings = [[['N','E'],['S','W']], [['N','S'],['E','W']], [['N','W'],['E','S']]];
function edgeKey(e) { return [...e].sort().join('-'); }
function validate(data) {
  const fail = msg => { throw new Error('HBK4-04 HOLD: ' + msg); };
  if (!data || data.schema !== 'hubcore-k4-v1' || data.system !== 'MonadMetatronSystem') fail('unsupported schema');
  const c = data.config || {};
  if (c.units !== 1 || c.bits !== 3 || c.nodes !== 4 || c.pairs !== 6) fail('configuration mismatch');
  if (data.reik_status !== '0 HOLD' || data.external_echo !== false) fail('evidence gate mismatch');
  if (!data.monad || data.monad.is_graph_vertex !== false || JSON.stringify(data.monad.xyz) !== '[0,0,0]') fail('monad boundary');
  if (!Array.isArray(data.vertices) || data.vertices.length !== 4) fail('four vertices required');
  const found = new Set();
  for (const v of data.vertices) {
    if (!v || !Object.hasOwn(coords, v.id) || found.has(v.id) || JSON.stringify(v.xyz) !== JSON.stringify(coords[v.id])) fail('vertex coordinates');
    found.add(v.id);
  }
  if (!Array.isArray(data.matchings) || data.matchings.length !== 3) fail('three matchings required');
  const allEdges = new Set();
  for (let i=0; i<3; i++) {
    const matching = data.matchings[i];
    if (!Array.isArray(matching) || matching.length !== 2) fail('matching size');
    const local = new Set();
    for (let j=0;j<2;j++) {
      const edge = matching[j];
      if (!Array.isArray(edge) || edge.length !== 2 || !found.has(edge[0]) || !found.has(edge[1]) || edge[0] === edge[1]) fail('invalid edge');
      local.add(edge[0]); local.add(edge[1]);
      const key=edgeKey(edge);
      if (allEdges.has(key) || key !== edgeKey(matchings[i][j])) fail('unexpected pair');
      allEdges.add(key);
    }
    if (local.size !== 4) fail('matching not disjoint');
  }
  if (allEdges.size !== 6) fail('K4 must have six pairs');
  if (!Array.isArray(data.states) || data.states.length !== 8) fail('eight states required');
  for (let n=0;n<8;n++) {
    const state = data.states[n], bits=n.toString(2).padStart(3,'0');
    if (!state || state.bits !== bits) fail('state order or bits');
    const expected=matchings.flatMap((m,i) => bits[i] === '1' ? m : []);
    if (!Array.isArray(state.edges) || state.edges.length !== expected.length ||
        state.edges.some((e,i)=>JSON.stringify(e)!==JSON.stringify(expected[i])) ||
        state.edge_count !== expected.length ||
        state.degree !== bits.split('1').length-1) fail('invalid state edges or degree');
  }
  for (const p of Object.values(coords)) for (const q of Object.values(coords)) {
    if (p === q) continue;
    if (p.reduce((sum,x,i)=>sum+(x-q[i])**2,0)!==8) fail('non-regular tetrahedron');
  }
  return true;
}
function load(file=DEFAULT_PATH) {
  const raw=fs.readFileSync(file);
  const sha256=crypto.createHash('sha256').update(raw).digest('hex');
  if (sha256!==PIN) throw new Error('HBK4-04 HOLD: original-byte SHA-256 mismatch');
  const data=JSON.parse(raw.toString('utf8'));
  validate(data);
  return data;
}
function consume(bits, file=DEFAULT_PATH) {
  if (!/^[01]{3}$/.test(bits)) throw new Error('HBK4-04 HOLD: expected exactly three Boolean bits');
  const data=load(file);
  const state=data.states.find(s=>s.bits===bits);
  return {schema:data.schema,system:data.system,config:data.config,monad:data.monad,
    vertices:data.vertices,edges:state.edges,bit_state:bits,edge_count:state.edge_count,
    node_degree:state.degree,reik_status:'0 HOLD',external_echo:false,
    deployment_verified:false,consumer:'local-only-opt-in'};
}
if (require.main===module) {
  const bits=process.argv[2] || '111';
  try { process.stdout.write(JSON.stringify(consume(bits))+'\n'); }
  catch(err) { process.stderr.write(err.message+'\n'); process.exitCode=1; }
}
module.exports={PIN,DEFAULT_PATH,validate,load,consume};
