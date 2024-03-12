#!/usr/bin/node
// Write a script that prints x times “C is fun”.

const x = process.argv;

if (!isNaN(x[2])) {
  const result = parseInt(x[2]);

  for (let i = 0; i < result; i++) {
    console.log('C is fun');
  }
}
