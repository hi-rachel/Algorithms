function solution(k, dungeons) {
    let result = [];
    let visited = Array(dungeons.length).fill(0);
    
    function dfs(cnt, k){
        result.push(cnt)
        
        for(let i = 0; i < dungeons.length; i++){
            let current = dungeons[i];
            if(k >= current[0] && !visited[i]){
                visited[i] = 1;
                dfs(cnt+1, k - current[1]);
                visited[i] = 0;
            }
        }
    }
    
    dfs(0, k);
    return Math.max(...result);
}


