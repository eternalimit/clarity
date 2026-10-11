'use strict';
const fs = require('fs');
const assert = require('assert');
const matching = [[['N','E'],['S','W']],[['N','S'],['E','W']],[['N','W'],['E','S']]];
const vertices = [{id:'N',xyz:[1,1,1]},{id:'E',xyz:[1,-1,-1]},{id:'S',xyz:[-1,1,-1]},{id:'W',xyz:[-1,-1,1]}];
const states = [];
for (let n=0;n<8;n++) {
  const bits=n.toString(2).padStart(3,'0');
  const edges=[];
  for (let k=0;k<3;k++) if (bits[k]==='1') edges.push(...matching[k]);
  states.push({bits,edges,edge_count:edges.length,degree:bits.split('1').length-1});
}
const value = {
  schema:'hubcore-k4-v1',system:'MonadMetatronSystem',
  config:{units:1,bits:3,nodes:4,pairs:6},
  bit_semantics:'three independent Boolean switches, not three-valued digits',
  monad:{is_graph_vertex:false,xyz:[0,0,0]},
  coordinate_claim:'constructed exact 3D embedding; not measured from generated art',
  vertices,matchings:matching,states,reik_status:'0 HOLD',external_echo:false
};
const actual=fs.readFileSync(process.argv[2] || 'research/hubcore/HBK4-03/coordinate_mapping.json','utf8');
const expected=JSON.stringify(value)+'\n';
assert.strictEqual(actual,expected,'Lua and JavaScript byte agreement');
const edges=new Set(matching.flat().map(e=>e.slice().sort().join('-')));
assert.strictEqual(edges.size,6);
assert.strictEqual(states.length,8);
assert.strictEqual(states[7].edge_count,6);
for (const v of vertices) {
 for (const w of vertices) if (v.id!==w.id) {
  assert.strictEqual(v.xyz.reduce((s,t,i)=>s+(t-w.xyz[i])**2,0),8);
 }
}
console.log(JSON.stringify({status:'PASS',states:8,edges:6,module_comparison:'byte-exact',external_echo:false}));
