function solution(numbers) {
    const answer = numbers.sort((a,b) => `${b}${a}` - `${a}${b}`);
    return answer[0] === 0 ? ""+answer[0] : answer.join('');
}