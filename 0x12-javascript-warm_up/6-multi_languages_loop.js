#!/usr/bin/node
// Write a script that prints 3 lines: (like 1-multi_languages.js)
// but by using an array of string and a loop

const firstLine = 'C is fun';
const secondLine = 'python is cool';
const thirdLine = 'JavaScript is amazing';

const myList = [
  firstLine,
  secondLine,
  thirdLine
];

for (let i = 0; i <= myList.length - 1; i++) {
  console.log(myList[i]);
}
