#!/usr/bin/node
// Write a script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object

function writeToAFile (filePath, content) {
  const fs = require('node:fs');
  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
      console.error({ error: error });
    }
  });
}
// Access the commandline args
const argvFilePath = process.argv[2];
const argvContent = process.argv[3];
writeToAFile(argvFilePath, argvContent);
