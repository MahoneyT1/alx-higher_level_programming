#!/usr/bin/node
/* Write a script that prints two arguments passed to it, in the
   following format is
*/

const args = process.argv;

const first = args[2];
const second = args[3];

console.log(`${first} ` + 'is' + ` ${second}`);
