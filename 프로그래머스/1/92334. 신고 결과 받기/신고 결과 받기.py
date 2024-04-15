# 각 유저는 한 번에 한 명의 유저를 신고할 수 있다. 신고 횟수에 제한은 x, 동일한 유저에 대한 신고 횟수는 1회로 처리됨

# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송

# 이용자, [이용자id, 신고한id 형태의 문자열], 
def solution(id_list, report, k):
    answer = []
    
    id_set_dict = {id_: set() for id_ in id_list}
    id_email_cnt = [0] * len(id_list)
    
    for i in range(len(report)):
        reporter, black = report[i].split()
        id_set_dict[black].add(reporter)
    
    for i in range(len(id_list)):
        if len(id_set_dict[id_list[i]]) >= k:
            for j in id_set_dict[id_list[i]]:
                id_email_cnt[id_list.index(j)] += 1
      
    # id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 된다.
    return id_email_cnt