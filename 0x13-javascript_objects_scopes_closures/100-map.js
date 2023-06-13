#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
function myfunc (num) {
  return num * list.indexOf(num);
}
const newList = list.map(myfunc);
console.log(newList);
