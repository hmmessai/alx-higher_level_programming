#!/usr/bin/node
const array = process.argv;
let max = parseInt(array[2]);
let i = 2;
function maximum (array) {
  if (array.length === 2 || array.length === 3) {
    return (0);
  }
  while (array[i] !== undefined) {
    if (parseInt(array[i]) > max) {
      max = array[i];
    }
    i++;
  }
  i = 2;
  let max2 = parseInt(array[2]);
  while (array[i] !== undefined) {
    if (parseInt(array[i]) !== max && parseInt(array[i]) > max2) {
      max2 = array[i];
    }
    i++;
  }
  return (max2);
}

console.log(maximum(array));
