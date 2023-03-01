function solution(n, computers) {
    let answer = 0;
    const length = computers.length;
    const visited = Array.from({length : n}, () => false);

    function dfs(idx) {
        visited[idx] = true;
        
        for (let i = 0; i < length; i++) {
            if (computers[idx][i] && !visited[i]) {
                dfs(i);
            }
        }
    }
    for (let i = 0; i < length; i++) {
        if (!visited[i]) {
            dfs(i);
            answer++;
        }
    }
    return answer;
}