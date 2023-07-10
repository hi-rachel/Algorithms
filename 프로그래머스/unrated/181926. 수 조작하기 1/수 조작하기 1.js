function solution(n, control) {
    const dict = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10
    }
    
    for (let c of control){
        n += dict[c];
    }
    return n;
}