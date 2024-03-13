#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if ((!isNaN(arg1) || !isNaN(arg2)) &&
  (Number.isInteger(arg1) || Number.isInteger(arg2))) {
  const first = parseInt(arg1, 10);
  const second = parseInt(arg2, 10);
  const sum = add(first, second);
  console.log(sum);
} else {
  console.log('NaN');
}
function add (a, b) {
  return a + b;
}
