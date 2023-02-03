function solution(brown, yellow) {
    let sum = brown + yellow;
    
    // 카펫의 최소높이 3
    for (let h = 3; h < Math.floor(brown/2); h++) {
        if (sum % h === 0) {
            let w = sum / h;
            
            // 테두리를 제외한 길이를 구해야하기 때문에 -2
            if ((h-2) * (w-2) === yellow) {
                return [w, h];
            }
        }
    }
}