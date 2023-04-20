const fs = require('fs');
let n = Number(fs.readFileSync('./dev/stdin').toString());
const mp = {1:1, 2:2};
for(let i = 3; i <= n; i++){
    mp[i] = (mp[i - 1] + mp[i - 2]) % 10007;
}
console.log(mp[n]);