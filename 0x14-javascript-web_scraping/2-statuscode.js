#!/usr/bin/node
// Write a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>
// You must use the module request#!/usr/bin/node
// Write a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>
// You must use the module request#!/usr/bin/node
// Write a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>

const req = require('request');

function displayStatus (url) {
  req(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log('code:', response.statusCode);
    }
  });
}
// extract the url from argv
const url = process.argv[2];
displayStatus(url);
