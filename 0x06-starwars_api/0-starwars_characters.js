#!/usr/bin/node

const request = require('request');

if (process.argv.length >= 3) {
  let filmId = process.argv[2];
  filmId = parseInt(filmId);
  if (Number.isInteger(filmId)) {
    request(`https://swapi-api.alx-tools.com/api/films/${filmId}`,
      function (error, response, body) {
        if (error) { return console.log(error); }
        if (!error && response.statusCode === 200) {
          const characters = JSON.parse(body).characters;
          const characterNames = characters.map(function (character) {
            const P = new Promise((resolve, reject) => {
              request(character, (err, res, bdy) => {
                if (!err) {
                  resolve(JSON.parse(bdy).name);
                } else {
                  reject(err);
                }
              });
            });
            return P;
          });
          Promise.all(characterNames)
            .then((char) => { console.log(char.join('\n')); })
            .catch(e => console.log(e));
        }
      }
    );
  }
}
