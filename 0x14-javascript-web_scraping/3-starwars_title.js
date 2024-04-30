#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie where the
// episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
// You must use the module request

function titleOfStarWar (id) {
  const req = require('request');
  const starWarApi = `https://swapi-api.alx-tools.com/api/films/${id}`;
  req(starWarApi, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const movieTitle = JSON.parse(body);
      console.log(movieTitle.title);
    }
  });
}

const episodeNumber = parseInt(process.argv[2]);
titleOfStarWar(episodeNumber);
