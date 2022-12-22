function solution(denum1, num1, denum2, num2) {
    let firstValue = denum1 * num2 + denum2 * num1;
    let secondValue = num1 * num2;
    let gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
    let min = gcd(firstValue, secondValue);
    return [firstValue / min, secondValue / min];
}

