function solution(cards1, cards2, goal) {
    for (let word of goal) {
        if (cards1.indexOf(word) === 0) {
            cards1.shift();
        }
        else if (cards2.indexOf(word) === 0) {
            cards2.shift();
        }
        else return "No";
    }
    return "Yes";
}