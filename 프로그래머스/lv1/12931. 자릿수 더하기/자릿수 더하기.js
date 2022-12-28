function solution(n) {
    let digits = n.toString().split('');
    let realDigits = digits.map(Number);
    return realDigits.reduce((a,b) => parseInt(a+b));
}