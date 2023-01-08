function solution(array) {
    let result = 0;
    array.toString().split('').map(x => x.includes('7') ? result++ : null);
    return result;
}