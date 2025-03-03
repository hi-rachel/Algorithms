def solution(schedules, timelogs, startday):
    gift = 0
    n = len(schedules)
    
    for idx, goal in enumerate(schedules):
        # 출근 마감 시간 계산 (goal + 10분)
        goal_hour = goal // 100
        goal_minute = goal % 100
        
        deadline_minute = goal_minute + 10
        deadline_hour = goal_hour + (deadline_minute // 60)
        deadline_minute %= 60
        
        deadline = deadline_hour * 100 + deadline_minute
        
        # 출근 상태 확인
        on_time_count = 0
        needed_days = 0
        current_day = startday
        
        for i in range(7):
            # 주말인 경우 건너뛰기
            if current_day in [6, 7]:
                current_day = 1 if current_day == 7 else current_day + 1
                continue
            
            # 평일인 경우 출근 체크
            needed_days += 1
            if timelogs[idx][i] <= deadline:
                on_time_count += 1
            
            # 평일 5일을 모두 확인했으면 종료
            if needed_days >= 5:
                break
                
            # 다음 날로 이동
            current_day = 1 if current_day == 7 else current_day + 1
        
        # 모든 평일에 지각하지 않았는지 확인
        if on_time_count == needed_days:
            gift += 1
    
    return gift