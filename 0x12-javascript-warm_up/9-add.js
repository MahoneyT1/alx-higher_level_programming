#!/usr/bin/node

const com = process.argv;

const first = parseInt(com[2]);
const second = parseInt(com[3]);

function add(a, b) {
    if ((a === NaN) || (b === NaN)) {
      return;
    }
    return a + b;
}

let sum = add(first, second);
console.log(sum);
