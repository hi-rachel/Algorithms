function solution(s){
    let count = 0;
    for(let test of s) {
        if (test == "(") count += 1;
        else count -= 1; if (count < 0) break;
    }
    return count != 0 ? false : true;
}
