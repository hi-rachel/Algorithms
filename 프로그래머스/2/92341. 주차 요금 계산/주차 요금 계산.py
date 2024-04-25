# 입차 후 출차 내역이 없다면 23:59에 출차된 것으로 간주
# 누적 주차 시간이 기본 시간 이하라면, 기본 요금 청구
# 초과하면, 초과한 시간에 대해서 단위 시간마다 단위 요금을 청구한다.
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림한다 = [a] = a보다 작지 않은 최소의 정수

# fees = [기본 시간, 기본 요금, 단위 시간, 단위 요금]
# record = [시각 차량번호 내역]
# 시각 = HH:MM 00:00 ~ 23:59

# 주차 요금 배열, 자동차 입/출차 내역을 나타내는 문자열 배열
import math

# 차량 번호가 작은 자동차부터 청구할 주차 요금 배열 만들기
def sort_car_num_pay(total_pay):
    return [value for key, value in sorted(total_pay.items())]

# 요금 기록
def pay_check(fees, total_pay):
    for key, val in total_pay.items(): 
        if val <= fees[0]: # 기본 시간 이하시
            total_pay[key] = fees[1] # 기본 요금
        else: # 초과시
            total_pay[key] = fees[1] + math.ceil((total_pay[key] - fees[0]) / fees[2]) * fees[3] # 단위 시간마다 추가 요금 부여
            
    return sort_car_num_pay(total_pay)

def solution(fees, records):
    record_dict = {}
    total_pay = {}
    
    for record in records:
        time, car_num, in_out = record.split()
        hour, minutes = map(int, time.split(':'))
        
        cal_time = hour * 60 + minutes
        
        if in_out == "IN":
            record_dict[car_num] = cal_time
        elif in_out == "OUT":
            total_time = cal_time - record_dict[car_num] # 출차 시간 - 입차 시간
            if car_num not in total_pay:
                total_pay[car_num] = 0
            total_pay[car_num] += total_time
            del record_dict[car_num]
            
    # 출차 기록이 없는 차량에 대해 23:59 출차로 처리
    end_day = 23 * 60 + 59
    for car_num, entry_time in record_dict.items():
        total_time = end_day - entry_time
        if car_num not in total_pay:
            total_pay[car_num] = 0
        total_pay[car_num] += total_time
            
    return pay_check(fees, total_pay)