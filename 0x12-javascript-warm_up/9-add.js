#!/usr/bin/node

const com = process.argv;

if (com.length < 4) {
  console.log(NaN);
}
const first = parseInt(com[2], 10);
const second = parseInt(com[3], 10);

function add (a, b) {
  if (isNaN(a) === true || isNaN(b) === true) {
    return NaN;
  } 
   return a + b;
}
const sum = add(first, second);
console.log(sum);
