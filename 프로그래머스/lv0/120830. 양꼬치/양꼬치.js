function solution(n, k) {
    let count = Math.floor(n / 10);
    return n >= 10 ? 12000 * n + 2000 * (k-count) : 12000 * n + 2000 * k;
}