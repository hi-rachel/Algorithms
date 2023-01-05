function solution(s1, s2) {
    let result = [];
    for (let i = 0; i <= s2.length; i++) {
        if (s1.includes(s2[i])) {
            result.push(s2[i]);
        }
    }
    return result.length;
}