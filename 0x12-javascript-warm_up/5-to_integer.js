#!/usr/bin/node

// Write a script that prints My number: <first argument converted
// in integer> if the first argument can be converted to an integer.

const args = process.argv;

if (!isNaN(args[2])) {
  const floorDiv = Math.floor(parseInt(args[2]));
  console.log('my first number: ', floorDiv);
} else {
  console.log('Not a number');
}
