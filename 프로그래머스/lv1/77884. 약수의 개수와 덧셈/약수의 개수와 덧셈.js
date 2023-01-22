function solution(left, right) {
    // 약수의 개수가 짝수인 수는 +
    // 약수의 개수가 홀수인 수는 -
    let result = [];
    for(let i = left; i <= right; i++) {
        let divide = [];
        for (let j = right; j >= 1; j--) {
            if (i % j == 0) divide.push(j);
        }
        if (divide.length % 2 == 0) result.push(i)
        else result.push(-i);
    }
    return result.reduce((acc, cur) => acc+cur);
}