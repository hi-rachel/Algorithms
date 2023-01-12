function solution(score) {
    let result = [];
    for (let test in score) {
            result.push(score[test].reduce((a,b) => (a + b / 2), 0));
        }
        const sorted = [...result].sort((a, b) => b - a);
        const rank = [...result].map((v) => sorted.indexOf(v)+1);
        return rank;
}