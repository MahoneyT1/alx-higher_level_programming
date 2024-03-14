#!/usr/bin/node
/*
 * Write a function that executes x times a function.
*/

exports.callMeMoby = function (x, theFuction) {
  for (let i = 0; i < x; i++) {
    theFuction();
  }
};
