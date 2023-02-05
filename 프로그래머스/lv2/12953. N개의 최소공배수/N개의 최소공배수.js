function gcd(a, b) {
    return !b ? a : gcd(b, a%b);
}

function lcm(a,b) {
    return (a*b) / gcd(a,b);
}

function solution(arr) {
    let answer = 1;
    for (let i = 0; i < arr.length; i++) {
        answer = lcm(answer, arr[i]);
    }
    return answer;
}
