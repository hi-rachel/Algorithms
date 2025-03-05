function solution(numbers, target) {
    let stack = [[0, 0]]
    let cnt = 0
    
    while (stack.length > 0) {
        let [idx, total] = stack.pop()
        
        if (idx === numbers.length) {
            if (total === target) {
                cnt += 1
            }
            continue
        }
        
        stack.push([idx+1, total+numbers[idx]])
        stack.push([idx+1, total-numbers[idx]])
    }
    return cnt
}