

def solution(numbers, target):
    answer = 0
    
    def dfs(num_idx, num_sum):
        if num_idx == len(numbers):
            if num_sum == target:
                nonlocal answer
                answer += 1
        
        else:
            dfs(num_idx+1, num_sum+numbers[num_idx])
            dfs(num_idx+1, num_sum-numbers[num_idx])
    
    
    dfs(0, 0);
    return answer