function solution(s) {
    let answer = [0, 0];
    while (s.length > 1) {
        // 이진 변환 횟수++
        answer[0]++;
        
        // s 안에 0의 갯수++
        answer[1] += (s.match(/0/g)||[]).length;
        
        // 0을 제거한 길이 이진 변환
        s = s.replace(/0/g, '').length.toString(2);
    }
    return answer;
}