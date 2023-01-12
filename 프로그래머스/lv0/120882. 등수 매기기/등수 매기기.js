function solution(score) {
    let result = [];
    for (let test in score) {
            result.push(score[test].reduce((a,b) => (a + b / 2), 0));
        }
        const sorted = result.slice().sort((a, b) => b - a);
        const rank = result.slice().map((v) => sorted.indexOf(v)+1);
        return rank;
}