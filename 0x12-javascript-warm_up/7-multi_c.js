#!/usr/bin/node
// Write a script that prints x times “C is fun”.

const x = process.argv[2];
const parsedIn = parseInt(x, 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parsedIn) {
    console.log('C is fun');
    i++;
  }
}
