#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let newStr;
    for (let i = 0; i < this.height; i++) {
      newStr = '';
      for (let j = 0; j < this.width; j++) {
        newStr += 'X';
      }
      console.log(newStr);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
