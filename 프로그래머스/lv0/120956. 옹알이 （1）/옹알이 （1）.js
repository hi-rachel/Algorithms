function solution(babbling) {
    let result = 0;
    
    for (let babyTalk of babbling) {
        if (/(aya|ye|woo|ma)\1+/g.test(babyTalk)) continue;
        
        if (/^(aya|ye|woo|ma)+$/g.test(babyTalk)) {
            result++;
        };
    }
    return result;
}
    
