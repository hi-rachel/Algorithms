function solution(n) {
    let count = 0;
    for (let i = 1; i < n/2 + 1; i++) {
        const sum = i * (i + 1) / 2;
        const sub = n - sum;
        if (sub < 0) break;
        if (sub % i === 0) {
            count++;
        }
    }
    return count;
}