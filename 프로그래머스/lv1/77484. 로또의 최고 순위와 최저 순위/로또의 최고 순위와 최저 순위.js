function solution(lottos, win_nums) {
    let cnt = 0;
    let chance = 0;
    
    for(let i = 0; i < lottos.length; i++){
        if(win_nums.includes(lottos[i])){
            cnt++;
        }
        if(lottos[i] == 0){
            chance++;
        }
    }
    
    const result = [];
    const rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6,
    };
    let maxCnt = cnt + chance;
    result.push(rank[maxCnt]);
    result.push(rank[cnt]);
    return result;
}