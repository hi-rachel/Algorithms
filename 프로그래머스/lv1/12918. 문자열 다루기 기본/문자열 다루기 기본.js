function solution(s) {
    const regex = /[A-Z]/gi;
    if (s.match(regex)) return false;
    else if (s.length != 4 && s.length != 6) return false;
    else return true;
}