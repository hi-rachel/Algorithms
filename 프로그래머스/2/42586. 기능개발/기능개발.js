/*
* 각 기능은 진도가 100%일 때 서비스에 반영 가능
* 뒤에 있는 기능이 먼저 개발되어도, 앞에 있는 기능이 배포될 때 함께 배포됨.
* 각 배포마다 몇 개의 기능이 배포되는지를 반환해라
*
* TC: O(N)
* SC: O(N)
*/

// 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열, 각 작업의 개발 속도가 적힌 정수 배열
function solution(progresses, speeds) {
    const days = progresses.map((p, i) => Math.ceil((100 - p) / speeds[i]));
    const answer = [];
    
    let prev = days[0];
    let cnt = 1;
    for (let i = 1; i < days.length; i++) {
        if (prev >= days[i]) {
            cnt += 1;
        } else {
            answer.push(cnt);
            prev = days[i];
            cnt = 1;
        }
    }
    answer.push(cnt);
    return answer;
}