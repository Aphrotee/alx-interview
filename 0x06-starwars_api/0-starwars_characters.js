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
          const jsonObject = JSON.parse(body);
          if (jsonObject !== undefined) {
            for (let i = 0; i < jsonObject.characters.length; i++) {
              request(jsonObject.characters[i],
                function (err, res, bdy) {
                  if (err) { return console.log(err); }
                  if (!err && res.statusCode === 200) {
                    const _jsonObject = JSON.parse(bdy);
                    console.log(_jsonObject.name);
                  }
                }
              );
            }
          }
        }
      }
    );
  }
}
