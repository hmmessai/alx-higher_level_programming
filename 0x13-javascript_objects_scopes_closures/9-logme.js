#!usr/bin/node
let narg = 0;
module.exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
