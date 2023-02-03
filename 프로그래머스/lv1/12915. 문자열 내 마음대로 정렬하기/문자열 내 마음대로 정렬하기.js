function solution(strings, n) {
    let answer = strings.sort(
    (a,b) => (a.charCodeAt(n) === b.charCodeAt(n)) ?
    (a > b ? 1 : -1) :
    (a.charCodeAt(n)-b.charCodeAt(n)))
    return answer;
}
