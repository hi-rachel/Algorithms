function solution(arr) {
    let min = [...arr].sort((a, b) => a - b)[0];
    let result = arr.filter((item) => item !== min);
    return result.length > 0 ? result : [-1];
}