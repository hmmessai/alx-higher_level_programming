#!/usr/bin/node
const array = process.argv;
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  const arr = array.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; });
  console.log(second[1]);
}
