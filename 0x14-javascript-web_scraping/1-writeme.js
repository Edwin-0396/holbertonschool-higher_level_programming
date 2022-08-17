#!/usr/bin/node
const fs = require('fs');

// write JSON string to a file
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    throw err;
  }
});
