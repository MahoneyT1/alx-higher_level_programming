#!/usr/bin/node
// Write a script that reads and prints the content of a file.
// Write a script that reads and prints the content of a file.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

async function readFromFile (filepath) {
  const fs = require('node:fs');
  const readData = fs.readFileSync(filepath, 'utf-8');
  console.log(readData);
}
// take arg from commandline
const fileP = process.argv[2];
readFromFile(fileP);
