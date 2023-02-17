function solution(s) {
    let answer = [];
    let clean = s.slice(2, -2).replace(/},{/g, " ").split(' ').sort((a,b) => a.length - b.length);
    clean.forEach(v => {
        let tuple = v.split(',');
        tuple.map(x => !answer.includes(x) ? answer.push(x) : null);
    });
    return answer.map(x => +x);
}