function solution(answers) {
    const one = [1, 2, 3, 4, 5];
    const two = [2, 1, 2, 3, 2, 4, 2, 5];
    const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let scores = [0, 0, 0];
    
    // 1, 2, 3번이 각 정답을 맞춘 횟수 = scores
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === one[i%5]) scores[0]++;
        if (answers[i] === two[i%8]) scores[1]++;
        if (answers[i] === three[i%10]) scores[2]++;
    }
    let result = [];
    const max = [Math.max.apply(null, scores)];
    for (let i = 0; i < scores.length; i++) {
        if (scores[i] == max) result.push(i+1);
    }
    return result;
}