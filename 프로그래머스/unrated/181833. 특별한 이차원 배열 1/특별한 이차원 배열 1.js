function solution(n) {
    // n x n 크기의 이차원 배열
    let result = [];
    for(let i = 0; i < n; i++){
        let ele = [];
        for(let j = 0; j < n; j++){
            if(i == j){
                ele.push(1);
            }else {
                ele.push(0);
            }
        }
        result.push(ele);
    }
    return result;
}