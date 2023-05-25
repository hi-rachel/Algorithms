const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const temp = input.split('').reverse().join('');

if(input == temp) {
    console.log(1);
} else {
    console.log(0);
}
