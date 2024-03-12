#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed.

const args = process.argv;
const lengthOfArgv = args.length;

if (lengthOfArgv >= 4) {
  console.log('Arguments found');
} else if (lengthOfArgv === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
