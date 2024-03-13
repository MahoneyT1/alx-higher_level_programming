#!/usr/bin/node

const com = process.argv;

const first = parseInt(com[2]);
const second = parseInt(com[3]);

function add(a, b) {
    if ((isNaN(a) || (isNaN(b)) {
      return NaN;
    }
    return a + b;
}

let sum = add(first, second);
console.log(sum);
