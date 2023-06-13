#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
}
module.exports = Square;
