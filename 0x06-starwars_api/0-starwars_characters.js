#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error fetching movie information');
    process.exit(1);
  }
  const characters = JSON.parse(body).characters;
  function printCharacterNames(characterUrls, index = 0) {
    if (index === characterUrls.length) {

      process.exit(0);
    }
    request(characterUrls[index], (charError, charResponse, charBody) => {
      if (charError || charResponse.statusCode !== 200) {
        console.error(`Error fetching character ${index + 1} information`);
        process.exit(1);
      }
      const characterName = JSON.parse(charBody).name;
      console.log(characterName);
      printCharacterNames(characterUrls, index + 1);
    });
  }
  printCharacterNames(characters);
});
