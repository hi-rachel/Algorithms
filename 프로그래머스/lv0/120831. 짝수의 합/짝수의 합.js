function solution(n) {
    const even = [];
    for (let i = 0; i <= n; i++) {
        if (i % 2 === 0) {
            even.push(i);
        }
    }
    return even.reduce((a, b) => a + b, 0);
}