function solution(numbers) {
    const first = numbers.reduce((a, b) => Math.max(a,b));
    let firstIndex = numbers.indexOf(first);
    numbers.splice(firstIndex, 1);
    const second = numbers.reduce((a, b) => Math.max(a,b));
    return first * second;
}