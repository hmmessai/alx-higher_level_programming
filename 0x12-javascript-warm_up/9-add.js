#!/usr/bin/node
function add (a, b) {
  const first = parseInt(a);
  const second = parseInt(b);
  console.log(first + second);
}
add(process.argv[2], process.argv[3]);
