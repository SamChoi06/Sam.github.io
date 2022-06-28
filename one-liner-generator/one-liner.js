const fs = require('fs');

const lib = fs.readFileSync('/Users/samchoi06/Documents/GitHub/Sam.github.io/week2/mission4/wk2_4_lib.py', 'utf8');

const oneliner = JSON.stringify(lib);
console.log(oneliner);
