function solution(n) {
    const aliquot = [];
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            aliquot.push(i);
        }
    }
    return aliquot.reduce((a, b) => a+b, 0);
}