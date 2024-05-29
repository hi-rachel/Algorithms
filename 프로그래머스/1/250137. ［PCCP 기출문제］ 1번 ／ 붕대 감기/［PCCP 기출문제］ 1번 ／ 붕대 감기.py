# t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복
# t초 연속으로 붕대를 감는데 성공한다면 y만큼의 체력을 추가 회복

# 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기 다시 사용, 연속 성공 시간 0 초기화

# 현재 체력이 0이하가 되면 캐릭터가 죽으며 더 이상 체력을 회복할 수 없음!

# 붕대감기 기술의 정보[시전 시간, 초당 회복량, 추가 회복량], 캐릭터가 가진 최대 체력,
# 몬스터 공격 패턴[공격 시간, 피해량]
def solution(bandage, health, attacks):
    max_health = health
    last_time = attacks[-1][0]+1
    attack_time = []
    success_cnt = 0
    
    for attack in attacks:
        attack_time.append(attack[0])
            
    for i in range(1, last_time):
        if health <= 0:
            break
        
        # 공격
        if i in attack_time:
            success_cnt = 0
            health -= attacks[attack_time.index(i)][1]
        else:
            # 공격받지 않는다면
            if health < max_health:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            success_cnt += 1
        
        if success_cnt == bandage[0]:
            if health < max_health:
                health += bandage[2]
                if health > max_health:
                    health = max_health
            success_cnt = 0
    
    # 캐릭터가 끝까지 생존할 수 있는지 구해라(남은 체력 or -1 반환)
    return health if health > 0 else -1