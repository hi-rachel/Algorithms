function solution(array, n) {
    let same = array.filter((x) => x === n);
    return same.length;
}