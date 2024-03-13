#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0 || !Number.isInteger(n)) {
    return 1;
  } else if (isNaN(n) || n <= 1 || !Number.isInteger(n)) {
    return 1;
  } else if (!isNaN(n) || n >= 1 || Number.isInteger(n)) {
    return n * factorial(n - 1);
  }
}

const first = process.argv[2];
const temp = parseInt(first);

if (!isNaN(temp) && Number.isInteger(temp)) {
  console.log(factorial(temp));
}
