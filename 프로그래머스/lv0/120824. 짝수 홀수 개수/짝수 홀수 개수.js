function solution(num_list) {
    const answer = [];
    let even = 0;
    let odd = 0;
    for (let num of num_list) {
        num % 2 == 0 ? even += 1 : odd += 1;
    }
    answer.push(even, odd);
    return answer;
}