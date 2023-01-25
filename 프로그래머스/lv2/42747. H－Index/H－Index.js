function solution(citations) {
    if (citations.length === 1) {
        return citations[0] === 0 ? 1 : 1;
    }

    const sorted = citations.sort((a,b) => b-a);

    let answer = sorted.filter((element, index) => element > index).length;
    
    // // 0, 1 => 내림차순 1, 0 일 때 문제
    if (sorted[0] == 1 && sorted[1] == 0) return answer++;
    else return answer;
}