const fs = require('fs');

const lib = fs.readFileSync('/Users/samchoi06/Documents/GitHub/Sam.github.io/week2/mission3/wk2_3_lib.py', 'utf8');

const oneliner = JSON.stringify(lib);
console.log(oneliner);
