function solution(n, m) {
    let r;
    for(var nm = n*m; r = n % m; n = m, m = r){}
    return [m, nm/m];
}