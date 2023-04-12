#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    let i = 0;
    while (i < this.height) {
      if (c !== undefined) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
      i++;
    }
  }
}

module.exports = Square;
