#!/usr/bin/node
const x = process.argv[2];
let i = parseInt(x);
if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
