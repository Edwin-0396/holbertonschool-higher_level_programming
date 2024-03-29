#!/usr/bin/node

const axios = require('axios').default;
const URL = process.argv[2];

/* async function getCharacter () {
  try {
    const response = await axios.get(URL);
    const data = response.data.results;
    const characters = [];
    for (let i = 0; i < data.length; i++) {
      characters.push(data[i].characters);
    }
    let count = 0;
    for (let j = 0; j < characters.length; j++) {
      for (let k = 0; k < characters[j].length; k++) {
        if (characters[j][k].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } catch (error) {
    console.error(error);
  }
}

getCharacter();
*/
axios.get(URL)
  .then((response) => {
    const films = response.data.results;
    let appearences = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          appearences++;
        }
      }
    }
    console.log(appearences);
  })
  .catch((error) => {
    console.log(error);
  });
