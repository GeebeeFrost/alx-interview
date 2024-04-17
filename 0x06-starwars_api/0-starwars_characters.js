#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieURL, (error, _response, body) => {
  if (error) return console.error(error);
  const movie = JSON.parse(body);
  const characters = movie.characters;
  printCharacters(0, characters);
});

function printCharacters(index, array) {
  if (index === array.length) return;
  request.get(array[index], (error, _response, body) => {
    if (error) return console.error(error);
    const character = JSON.parse(body);
    console.log(character.name);
    printCharacters(index + 1, array);
  });
}
