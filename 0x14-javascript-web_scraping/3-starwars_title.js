#!/usr/bin/node

/**
 * Write a script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 * The first argument is the movie ID
 * You must use the Star wars API with the
 * endpoint https://swapi-api.alx-tools.com/api/films/:id
 * You must use the module request
*/

const request = require('request');
const movieId = parseInt(process.argv[2]);
const baseApiEndPoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getMovie (baseApiEndPoint) {
  request.get(baseApiEndPoint, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}
getMovie(baseApiEndPoint);
