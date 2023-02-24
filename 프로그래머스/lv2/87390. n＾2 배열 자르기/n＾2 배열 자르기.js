// function solution(n, left, right) {
//     const ans = [];
    
//     while(left <= right) {
//         ans.push(Math.max(Math.floor(left / n), left++ % n) + 1);
//     }
//     return ans;
// }

function solution(n, left, right) {
    const ans = [];
    
    for (let i = left; i <= right; i++) {
        const share = parseInt(i/n);
        const reminder = i%n;
        ans.push(Math.max(share, reminder) + 1)
    }
    return ans;
}