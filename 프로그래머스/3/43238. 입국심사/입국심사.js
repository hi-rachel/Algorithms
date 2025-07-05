function solution(n, times) {
    let start = 1
    let end = Math.max(...times) * n
    let answer = end;
    
    while (start <= end) {
        let mid = Math.floor((start + end) / 2)
        let total = 0
        // 각 심사관마다 심사할 수 있는 인원
        for (let time of times) {
            total += Math.floor(mid / time)
        }
        
        if (total >= n) {
            answer = mid
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    
    return answer
}