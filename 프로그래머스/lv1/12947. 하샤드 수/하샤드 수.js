function solution(x) {
    // 하샤드 수이려면 x의 자릿수 합으로 x가 나눠져야 함
    const prove = x.toString().split('').reduce((acc,cur) => acc + +cur, 0);
    if (x % prove == 0) {
        return true
    } return false
}