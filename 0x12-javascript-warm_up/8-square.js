#!/usr/bin/node
// Write a script that prints a square.

const first = process.argv[2];
const result = parseInt(first, 10);

// check if input is Not a Number or else
if (isNaN(result)) {
  console.log('Missing size');
} else {
  // loop along the length passed
  let i = 0;
  while (i < result) {
    // print x, using repeat function log (passed value) on
    // the same line, making it look like 2D array
    console.log('x'.repeat(result));
    i++;
  }
}
