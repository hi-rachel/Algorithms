function solution(s) {
    let answer = s.length;
    
    for(let i = 1; i <= Math.floor(s.length / 2); i++){
        let unit = '';
        let idx = 0;
        
        while(idx < s.length){
            let cnt = 1;
            while(s.slice(idx, idx+i) === s.slice(idx+i, idx+i+i)){
                cnt++;
                idx += i;
            }
            if(cnt > 1){
                unit += cnt;
            }
            const str = s.slice(idx, idx+i);
            unit = unit + str;
            idx += i;
        }
        answer = Math.min(answer, unit.length);
    }
    return answer;
}