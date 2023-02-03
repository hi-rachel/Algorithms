function solution(brown, yellow) {
    let sum = brown + yellow;
    
    for (let h = 3; h <= brown; h++) {
        if (sum % h === 0) {
            let w = sum / h;
            
            // 테두리를 제외한 길이를 구해야하기 때문에 -2
            if ((h-2) * (w-2) === yellow) {
                return [w, h];
            }
        }
    }
}