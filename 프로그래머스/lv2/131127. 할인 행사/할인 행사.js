function solution(want, number, discount) {
    let cnt = 0;
    
    const isMatch = (arr) => {
        let map = new Map();
        arr.forEach(v => map.set(v, (map.get(v)||0)+1));
        for(let i = 0; i < want.length; i++){
            if(map.get(want[i]) !== number[i]) return false;
        }
        return true;
    }
    
    for(let j = 0; j <= discount.length - 10; j++){
        let arr = discount.slice(j, j+10);
        if(isMatch(arr)){
            cnt++;
        }
    }
    return cnt;
}