#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((item, index) => index * item);
console.log(newList);
