function solution(a, b) {
    return a.reduce((total, val, idx) => total + val * b[idx], 0); 
}