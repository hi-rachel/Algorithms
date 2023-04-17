function solution(k, score) {
    let high = [];
    let result = [];
    let rank = high.sort((a,b) => a-b);
    for(let i = 0; i < score.length; i++){
        high.push(score[i]);
        high.sort((a,b) => a-b);
        if(high.length > k){
            high.shift();
            
        }
        result.push(high[0]);
    }
    return result;
}