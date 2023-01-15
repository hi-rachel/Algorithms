function solution(x, n) {
    let arr = Array.from({length: n+1}, (_, i) => i * x);
    return arr.splice(1, n);
}