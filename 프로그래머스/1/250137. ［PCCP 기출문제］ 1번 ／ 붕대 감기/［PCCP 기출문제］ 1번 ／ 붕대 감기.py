def solution(bandage, health, attacks):
    max_health = health
    last_time = attacks[-1][0] + 1
    attack_time_set = set()
    success_cnt = 0

    for attack in attacks:
        attack_time_set.add(attack[0])


    attack_dict = {attack[0]: attack[1] for attack in attacks}
    print(attack_dict)

    for i in range(1, last_time):
        # 죽으면 게임 끝
        if health <= 0:
            break

        # 공격
        if i in attack_time_set:
            success_cnt = 0
            health -= attack_dict[i]
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