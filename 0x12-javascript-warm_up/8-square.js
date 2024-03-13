#!/usr/bin/node

const arg = process.argv;

// check if input is Not a Number or else
if (isNaN(arg[2])) {
  console.log('Missing size');
} else {
  const counter = parseInt(arg[2], 10);
  for (let i = 0; i < counter; i++) {
    let check = '';
    for (let j = 0; j < counter; j++) {
      check += 'x' + '';
    }
    console.log(check);
  }
}
