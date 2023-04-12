#!/usr/bin/node
const size = process.argv[2];
const sqsize = parseInt(size);
if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqsize; i++) {
    console.log('X'.repeat(sqsize));
  }
}
