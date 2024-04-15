from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    # 각 유저가 신고한 이용자들을 저장하는 딕셔너리
    report_dict = defaultdict(set)
    # 각 유저가 받은 신고 횟수를 저장하는 딕셔너리
    report_count = defaultdict(int)

    # 신고 기록을 파싱하여 딕셔너리에 저장
    for r in report:
        reporter, reported = r.split()
        # 신고자가 이미 해당 유저를 신고한 경우를 제외하기 위해 집합을 사용
        if reported not in report_dict[reporter]:
            report_dict[reporter].add(reported)
            report_count[reported] += 1

    # 정지된 유저를 파악하여 해당 유저를 신고한 유저들에게 결과 메일을 전송
    for user in id_list:
        suspended_count = sum(1 for reported_user in report_dict[user] if report_count[reported_user] >= k)
        answer.append(suspended_count)

    return answer