#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

function getContent (url, filePath) {
  const request = require('request');
  const fs = require('node:fs');

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (error) => {
        if (error) {
          console.error('Error:', error);
        }
        console.log('successfull');
      });
    }
  });
}

const argvUrl = process.argv[2];
const argvfilePath = process.argv[3];
getContent(argvUrl, argvfilePath);
