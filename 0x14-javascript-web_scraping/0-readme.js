#!/usr/bin/node

/*
* Write a script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object
*/
const fs = require('fs').promises;

const commandArgs = process.argv;
const filePath = commandArgs[2];

async function readFileContent () {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

readFileContent();
