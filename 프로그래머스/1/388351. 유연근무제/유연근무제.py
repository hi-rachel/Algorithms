def solution(schedules, timelogs, startday):
    gift = 0
    n = len(schedules)
    
    for idx, goal in enumerate(schedules):
        cnt = 0
        week = startday
        workdays = 0
        
        # Calculate deadline time (goal + 10 minutes)
        goal_hour = goal // 100
        goal_minute = goal % 100
        
        # Add 10 minutes and handle hour overflow
        deadline_minute = goal_minute + 10
        deadline_hour = goal_hour + (deadline_minute // 60)
        deadline_minute %= 60
        
        deadline = deadline_hour * 100 + deadline_minute
        
        for i in range(7):
            if week in [6, 7]:  # Weekend
                week = 1 if week == 7 else week + 1
                continue
            
            # Check if employee arrived on time
            if timelogs[idx][i] <= deadline:
                cnt += 1
            
            workdays += 1
            
            if workdays >= 5:  # We've checked all weekdays
                break
            
            week = 1 if week == 7 else week + 1  
            
        if cnt == workdays:  # All weekdays were attended on time
            gift += 1
    
    return gift