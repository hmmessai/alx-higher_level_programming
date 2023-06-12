#!/usr/bin/node
const sqsize = parseInt(process.argv[2]);
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqsize; i++) {
    console.log('X'.repeat(sqsize));
  }
}
