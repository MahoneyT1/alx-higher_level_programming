#!/usr/bin/node

let argumentCounter = 0;

exports.logMe = function (item) {
  console.log(`${argumentCounter}: ${item}`);
  argumentCounter++;
};
