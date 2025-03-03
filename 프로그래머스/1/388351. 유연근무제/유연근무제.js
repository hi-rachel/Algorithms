function solution(schedules, timelogs, startday) {
    let gift = 0;
    const n = schedules.length;
    
    for (let idx = 0; idx < n; idx++) {
        const goal = schedules[idx];
        
        // 출근 마감 시간 계산 (goal + 10분)
        const goalHour = Math.floor(goal / 100);
        const goalMinute = goal % 100;
        
        let deadlineMinute = goalMinute + 10;
        let deadlineHour = goalHour + Math.floor(deadlineMinute / 60);
        deadlineMinute %= 60;
        
        const deadline = deadlineHour * 100 + deadlineMinute;
        
        // 출근 상태 확인
        let onTimeCount = 0;
        let neededDays = 0;
        let currentDay = startday;
        
        for (let i = 0; i < 7; i++) {
            // 주말인 경우 건너뛰기
            if (currentDay === 6 || currentDay === 7) {
                currentDay = currentDay === 7 ? 1 : currentDay + 1;
                continue;
            }
            
            // 평일인 경우 출근 체크
            neededDays++;
            if (timelogs[idx][i] <= deadline) {
                onTimeCount++;
            }
            
            // 평일 5일을 모두 확인했으면 종료
            if (neededDays >= 5) {
                break;
            }
                
            // 다음 날로 이동
            currentDay = currentDay === 7 ? 1 : currentDay + 1;
        }
        
        // 모든 평일에 지각하지 않았는지 확인
        if (onTimeCount === neededDays) {
            gift++;
        }
    }
    
    return gift;
}