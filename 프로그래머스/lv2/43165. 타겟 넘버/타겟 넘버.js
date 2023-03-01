function solution(numbers, target) {
    let answer = 0;
    const length = numbers.length;

    function DFS(count, sum) {
        if (count === length) {
            if (sum === target) {
                answer++;
            }
        } else {
            DFS(count + 1, sum + numbers[count]);
            DFS(count + 1, sum - numbers[count]);
        }
    }
    DFS(0, 0);
    return answer;
}