#!/usr/bin/node
/*
* Write a script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object
*/

const fs = require('fs').promises;

const stringArg = process.argv[3];
const filePath = process.argv[2];

async function writeToFile (filePath, stringArg) {
  try {
    await fs.writeFile(filePath, stringArg, 'utf-8');
  } catch (error) {
    console.error(error);
  }
}
writeToFile(filePath, stringArg);
