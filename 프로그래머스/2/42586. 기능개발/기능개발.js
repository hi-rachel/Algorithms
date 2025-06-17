/*
* 각 기능은 진도가 100%일 때 서비스에 반영 가능
* 뒤에 있는 기능이 먼저 개발되어도, 앞에 있는 기능이 배포될 때 함께 배포됨.
* 각 배포마다 몇 개의 기능이 배포되는지를 반환해라
*/

// 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열, 각 작업의 개발 속도가 적힌 정수 배열
function solution(progresses, speeds) {
    if (progresses.length == 1) {
        return [1]
    }
    
    const dates = [];
    const answer = [];
    let deploy = 0;
    for (let i = 0; i < progresses.length; i++) {
        // 남은 진도율이 걸리는 날짜
        let date = Math.ceil((100 - progresses[i]) / speeds[i]);
        if (dates.length === 0) {
            deploy += 1
            dates.push(date)
            continue
        }
        if (dates[dates.length - 1] >= date) {
            deploy += 1   
        } else {
            answer.push(deploy)
            deploy = 1
            dates.push(date)
        }
        if (i === (progresses.length - 1)) {
            answer.push(deploy)
        }
    }
    
    return answer;
}