function solution(picks, minerals) {
    let answer = 0;
    
    // 곡괭이 하나당 5개씩 캠
    let len = Math.ceil(minerals.length / 5);
    
    // 곡괭이 수
    let maxLen = picks.reduce((a, b) => a + b);
    
    let arr = [];
    
    if(maxLen === 0) return 0;
    
    // 캘 수 없는 광물 삭제
    minerals = minerals.splice(0, maxLen * 5);
    
    for(let i = 0; i < len; i++){
        // diamond, iron, stone 순
        let obj = {d: 0, i: 0, s: 0};
        // 5개씩 배열을 순회하며 obj에 카운터
        minerals.splice(0, 5).map((v) => obj[v[0]]++);
        // 각 피로도 추가
        arr.push([
            obj.d + obj.i + obj.s,
            obj.d * 5 + obj.i + obj.s,
            obj.d * 25 + obj.i * 5 + obj.s,
        ]);
    }

    // 가장 큰 값 stone 순으로 내림차순 후 diamond, 철, 돌 곡괭이 순으로 사용
    arr
    .sort((a, b) => b[2] - a[2])
    .map((v) => {
        if(picks[0] > 0) return picks[0]--, (answer += v[0]);
        if(picks[1] > 0) return picks[1]--, (answer += v[1]);
        if(picks[2] > 0) return picks[2]--, (answer += v[2]);
    });
    return answer;
}