function solution(my_string) {
    var answer = '';
    for (let char of my_string) {
        if (char.toUpperCase() === char) {
            answer += char.toLowerCase();
        } else {
            answer += char.toUpperCase();
        }
    }
    return answer;
}