function solution(arr, divisor) {
    let result = [];
    arr.map(x => x % divisor === 0 ? result.push(x) : null);
    return result.length > 0 ? result.sort((a,b) => a-b) : [-1];
}