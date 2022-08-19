#!/usr/bin/node
const axios = require('axios').default;
const id = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

axios.get(`${URL}${id}`)
  .then((response) => {
    console.log(response.data.title);
  })
  .catch((error) => {
    console.log(error.response.data.detail);
  })
  .then(() => {
  });
