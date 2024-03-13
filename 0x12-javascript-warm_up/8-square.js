#!/usr/bin/node

const arg = process.argv;

// check if input is Not a Number or else
if (isNaN(arg[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i <= arg.length; i++) {
    let strCon = '';
    for (let j = 0; j <= arg.length; j++) {
      strCon += 'x' + ' ';
    }
    console.log(strCon);
  }
}
