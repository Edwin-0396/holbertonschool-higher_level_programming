#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');
const URL = process.argv[2];
const file = process.argv[3];

async function storeWeb () {
  try {
    const response = await axios.get(URL);
    fs.writeFile(file, response.data, err => {
      if (err) {
        console.error(err);
      }
    });
  } catch (error) {
    console.error(error);
  }
}

storeWeb();
