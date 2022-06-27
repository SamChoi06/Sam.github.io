const fs = require('fs');

const lib = fs.readFileSync('../week2/mission1/wk2_1_lib.py', 'utf8');

const oneliner = JSON.stringify(lib);
console.log(oneliner);
