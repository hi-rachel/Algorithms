function solution(a, b) {
    if (a === b) return a;
    let result = [];
    if (a > b) {
        let lesser = b;
        b = a;
        a = lesser;
    }
    for (let i = a; i <= b; i++) {
        result.push(i);
    }
    return result.reduce((acc, cur) => acc + cur, 0);
}