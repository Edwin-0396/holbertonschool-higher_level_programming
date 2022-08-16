#!/usr/bin/node
exports.esrever = function (list) {
  const reversedArray = [];

  for (const rev in list) {
    reversedArray[rev] = list[list.length - rev - 1];
  }
  return (reversedArray);
};
