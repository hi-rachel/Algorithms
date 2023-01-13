function solution(i, j, k) {
    let result = 0;
    for (let count = i; count <= j; count++) {
        count.toString().split('').map(x => x.includes(k) === true ? result++ : null);
    }
    return result;
}
