function solution(seoul) {
    let index = 0;
    seoul.map(x => x === "Kim" ? index = seoul.indexOf(x) : 0);
    return `김서방은 ${index}에 있다`
}