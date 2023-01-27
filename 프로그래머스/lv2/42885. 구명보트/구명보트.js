function solution(people, limit) {
    // 구명보트를 최대한 적게 사용!하여 모든 사람을 구출
    // 구명보트 한 번에 최대 두명
    // 무거운 사람 순 정렬
    let sorted = people.sort((a,b) => (b-a));
    let answer = 0;
    let first = 0;
    let second = sorted.length - 1;

    while (first <= second) {
        if (sorted[first] <= limit /2) {
            answer += Math.ceil((second + 1 - first) / 2);
            break;
        }
        answer++;
        switch(sorted[first] + sorted[second] <= limit) {
            case true:
                first++;
                second--;
                break;
            case false:
                first++;
                break;
        }
    }
    return answer;
}