#!/usr/bin/node

const FirstSquare = require('./5-square');
module.exports = class Square extends FirstSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
