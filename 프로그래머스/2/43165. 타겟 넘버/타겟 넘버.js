function solution(numbers, target) {
    let count = 0
    const length = numbers.length;
    
    function dfs(idx, total) {
        if (idx === length) {
            if (total === target) {
                count += 1
            }
            return
        }
        
        dfs(idx+1, total+numbers[idx])
        dfs(idx+1, total-numbers[idx])
    }
    dfs(0, 0)
    return count
}