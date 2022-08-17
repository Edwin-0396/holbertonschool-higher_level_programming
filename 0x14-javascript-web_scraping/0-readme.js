#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    throw err;
  }
  console.log(data);
});
