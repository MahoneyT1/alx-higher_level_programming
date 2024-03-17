#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let match = 0;
  for (let i = 0; i <= list.length; i++) {
    if (list[i] === searchElement) {
      match += 1;
    }
  }
  return match;
};
