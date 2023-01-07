function solution(n) {
    let z = Math.sqrt(n);
    return n == Math.ceil(z) * Math.floor(z) ? 1 : 2;
}