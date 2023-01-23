function solution(n) {
    let count = 0;
    for (let i = 0; i <= n; i++) {
        // i는 n의 약수이면서 홀수인 개수
        if (n % i == 0 && i % 2 == 1) count++;
    }
    return count;
}