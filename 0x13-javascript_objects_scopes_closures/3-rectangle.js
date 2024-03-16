#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    if (this.width && this.height) {
      let newStr;
      for (let i = 0; i < this.height; i++) {
        newStr = '';
        for (let j = 0; j < this.width; j++) {
          newStr += 'x';
        }
        console.log(newStr);
      }
    }
  }
}
module.exports = Rectangle;
