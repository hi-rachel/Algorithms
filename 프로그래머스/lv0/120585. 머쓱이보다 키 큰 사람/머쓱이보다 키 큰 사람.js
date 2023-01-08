function solution(array, height) {
    let result = 0;
    for (let i = 0; i<array.length; i++) {
        array[i] > height ? result++ : null;
    }
    return result;
}