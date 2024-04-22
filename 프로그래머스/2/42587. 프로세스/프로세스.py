def solution(priorities, location):  
    cnt = 0
    while True:
        max_process = max(priorities) # 가장 우선순위가 높은 프로세스
        process = priorities.pop(0) # 맨 앞 프로세스 꺼내기
        
        if process == max_process: # 꺼낸 프로세스가 가장 우선순위가 높다면
            cnt += 1 # 실행
            if location == 0: # 순서가 다다르면 실행 순서 출력
                return cnt
        else:
            priorities.append(process) # 가장 우선순위가 높지 않다면 다시 대기 큐에 넣기
        location -= 1
            
        if location == -1:
            location = len(priorities) - 1
    