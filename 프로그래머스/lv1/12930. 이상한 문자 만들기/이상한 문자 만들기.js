function solution(s) {
    let words = s.split(' ');
    let answer = '';
    let answerSpace = [];
    
    words.forEach(function(word) {
        for (let i = 0; i < word.length; i++) {
            answer += i % 2 == 0 ? word[i].toUpperCase() : word[i].toLowerCase();
            
        }
        answerSpace.push(answer);
        answer = '';
    })
    return answerSpace.join(' ');
}