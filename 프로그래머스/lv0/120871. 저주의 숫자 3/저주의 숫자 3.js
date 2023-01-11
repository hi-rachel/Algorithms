function solution(n) {
    let result = 0;
    for (let i = 1; i <= n; i++) {
        result += 1;
        while (result % 3 === 0 | result.toString().includes(3)) {
            result += 1;
        }
    }
    return result;
}