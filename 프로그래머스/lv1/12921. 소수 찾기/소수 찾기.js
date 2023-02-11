function solution(n) {
    let result = new Array(n);
    if (n == 2) return 1;
    // n 범위
    for (let i = 2; i <= n; i++) {
        result[i] = i;
    }

    for (let i = 2; i <= n; i++) {
        if(result[i] == 0) continue;
        // 2부터 시작 특정 수의 배수에 해당하는 수는 모두 지워줌
        for (let j = i+i; j <= n; j += i) {
            result[j] = 0;
        }
    } 
    return result.filter(x => x !== 0).length
}
