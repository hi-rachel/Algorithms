function solution(n) {
    let isInt = Math.sqrt(n);
    if (isInt - Math.floor(isInt) != 0) {
        return -1;
    } else {
        return (isInt+1)**2;
    }
}