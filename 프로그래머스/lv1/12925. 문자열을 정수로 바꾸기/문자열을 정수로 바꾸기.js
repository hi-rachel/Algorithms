function solution(s) {
    if (s.includes('-')) {
        return - +(s.split('').splice(1).join(''))
    } else {
        return + +(s.split('').join(''))
    }
}