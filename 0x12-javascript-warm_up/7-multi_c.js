#!/usr/bin/node
// Write a script that prints x times “C is fun”.

const x = process.argv[2];

if (!isNaN(x)) {
  const result = parseInt(x);

  if (Number.isInteger(result) && result >= 0) {
    for (let i = 0; i < result; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
