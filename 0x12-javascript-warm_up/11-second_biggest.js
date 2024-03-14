#!/usr/bin/node

const arg = process.argv;

if (arg.length === 2) {
  console.log(0);
} else if (arg.length === 3) {
  console.log(0);
} else {
  const newL = Array.from(new Set(process.argv.slice(2)));
  newL.sort((a, b) => b - a);

  if (newL.length > 1) {
    console.log(newL[1]);
  }
}
