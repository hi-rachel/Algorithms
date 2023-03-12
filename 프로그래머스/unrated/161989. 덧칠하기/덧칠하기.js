function solution(n, m, section) {
    let answer = 0;
    let walls = [];
    
    if (section.length == 1) {
            return 1;
        }
    
    // 1미터로 나눈 벽들
    for (let i = 1; i <= n; i++) {
        walls.push(i);
    }
    
    // 페인트 칠하기
    while(section.length != 0) {
            if (m == 1) {
                answer += section.length;
                break;
            }
            let roller = section[0] + m - 1;
            section = section.filter(x => x > roller);
            answer++;
        }
    if (section.length == 1) answer++;
    return answer;
}