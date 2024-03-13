#!/usr/bin/node

function add (a, b) {
  if (Number.isInteger(a) || Number.isInteger(b)) {
    return a + b;
  }
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  const first = parseInt(arg1);
  const second = parseInt(arg2);
  const result = add(first, second);
  console.log(result);
}
