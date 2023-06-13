#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const line of list) {
    if (line === searchElement) {
      count++;
    }
  }
  return (count);
};
