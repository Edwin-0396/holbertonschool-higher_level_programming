#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const search in list) {
    if (list[search] === searchElement) {
      count++;
    }
  }
  return (count);
};
