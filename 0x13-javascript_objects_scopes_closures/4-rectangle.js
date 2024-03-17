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
        newStr += 'x';
      }
      console.log(newStr);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
