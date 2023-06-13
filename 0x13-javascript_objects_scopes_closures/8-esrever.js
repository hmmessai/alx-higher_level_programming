#!/usr/bin/node
module.exports.esrever = function (list) {
  let i = list.length - 1;
  const newList = [];
  while (i >= 0) {
    newList.push(list[i]);
    i--;
  }
  return (newList);
};
