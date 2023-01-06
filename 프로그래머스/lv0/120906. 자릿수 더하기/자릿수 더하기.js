function solution(n) {
    const nArr = n.toString().split('');
    let result = 0;
    for (let num of nArr) {
    result += +num;
    }
    return result;
}