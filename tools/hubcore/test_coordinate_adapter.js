'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const adapter=require('./coordinate_adapter');
let passes=0;
function test(fn) { fn(); passes++; }
function reject(fn) { test(()=>assert.throws(fn,/HOLD|SyntaxError/)); }
const original=adapter.load();
const clone=()=>JSON.parse(JSON.stringify(original));
test(()=>assert.equal(adapter.PIN,'031e6fa2af07a35c9ac48153a65c5c5e9090c36aa54a1816c54592b9b9cc092c'));
test(()=>assert.equal(adapter.validate(original),true));
test(()=>assert.equal(adapter.load().states.length,8));
for (let n=0;n<8;n++) {
  const bits=n.toString(2).padStart(3,'0');
  test(()=>assert.equal(adapter.consume(bits).bit_state,bits));
  test(()=>assert.equal(adapter.consume(bits).edge_count,2*bits.split('1').length-2));
  test(()=>assert.equal(adapter.consume(bits).node_degree,bits.split('1').length-1));
}
for(const b of ['','0','00','0000','222','01U','111\n','abc','-1']) reject(()=>adapter.consume(b));
const muts=[
 d=>{d.config.bits=4;},d=>{d.config.nodes=5;},d=>{d.config.pairs=7;},
 d=>{d.schema='hubcore-k4-v2';},d=>{d.reik_status='1';},
 d=>{d.external_echo=true;},d=>{d.monad.is_graph_vertex=true;},
 d=>{d.monad.xyz=[1,0,0];},d=>{d.vertices[0].xyz=[2,1,1];},
 d=>{d.vertices.push(d.vertices[0]);},d=>{d.matchings[0][0]=['N','N'];},
 d=>{d.matchings[0][0]=['E','S'];},d=>{d.states[0].edges=[['N','E']];},
 d=>{d.states[1].degree=3;},d=>{d.states[7].edge_count=5;},
 d=>{d.states[0].bits='111';},d=>{d.states.pop();}
];
for (const mutate of muts) reject(()=>{const x=clone();mutate(x);adapter.validate(x);});
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'hbk4-04-'));
try {
  const tampered=path.join(tmp,'coordinates.json');
  fs.writeFileSync(tampered,JSON.stringify(original)+'\n ');
  reject(()=>adapter.load(tampered));
  reject(()=>adapter.consume('111',tampered));
  fs.writeFileSync(tampered,'{');
  reject(()=>adapter.load(tampered));
} finally {fs.rmSync(tmp,{recursive:true,force:true});}
test(()=>assert.equal(adapter.consume('111').deployment_verified,false));
test(()=>assert.equal(adapter.consume('111').external_echo,false));
console.log(JSON.stringify({status:'PASS',assertions:passes,independent_echo:false,deployed:false}));
