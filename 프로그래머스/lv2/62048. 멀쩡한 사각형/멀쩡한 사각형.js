function solution(w, h) {
    // 겹치는 갯수 = 전체 갯수 - (가로 + 세로 - 최대공약수)
    let gcd = 1;
    for (let i = 1;  i <= Math.min(w, h); i++) {
        if (w % i == 0 && h % i == 0) {
            gcd = i;
        }
    }
    return w * h - (w + h - gcd);
}