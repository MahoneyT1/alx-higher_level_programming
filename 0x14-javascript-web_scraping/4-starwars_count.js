#!/usr/bin/node
// Write a script that prints the number of movies where
// the character “Wedge Antilles” is present.

// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// You must use the module request

function numberOfMovies (url) {
  let count = 0;
  // import request
  const request = require('request');

  // send a request to the received api
  request(url, (error, response, body) => {
    // check if there's error while making the request
    if (error) {
      // print to standard error the error output
      console.error('Error:', error);
    } else {
      const receivedData = JSON.parse(body);

      // loop through the receivedData and capture characters
      for (let i = 0; i < receivedData.results.length; i++) {
        if (Object.prototype.hasOwnProperty.call(receivedData.results[i], 'characters')) {
          const listOfCharacters = receivedData.results[i].characters;

          // create an end point, and check if the id 18 is present in the list
          const urlToId = 'https://swapi-api.alx-tools.com/api/people/18/';

          // loop and increment count if the url matches any url in the list
          for (let j = 1; j <= listOfCharacters.length; j++) {
            if (listOfCharacters[j] === urlToId) {
              count++;
            }
          }
        }
      }
      console.log(count);
    }
  });
}
const argvApi = process.argv[2];
numberOfMovies(argvApi);
