
# 빈칸 '.', 파일 '#'
# 최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일을 선택해서 한 번에 지우려고 한다.
# 시작점 S(lux, luy) - 사각형 왼쪽 위 -> E(rdx, rdy) - 사각형 오른쪽 아래
# 드래그 한 거리 = |rdx - lux| + |rdy - luy|

# 컴퓨터 바탕화면의 상태를 나타내는 문자열 배열
def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                lux = min(lux, x)
                luy = min(luy, y)
                   
                rdx = max(rdx, x+1)
                rdy = max(rdy, y+1)
                
    answer = [lux, luy, rdx, rdy]
    # 바탕 화면의 파일들을 한 번에 삭제하기 위해 최소한의 이동거리를 갖는 드래그의 시작점과 끝점을 담은 정수         배열을 반환해라 [lux, luy, rdx, rdy]
    return answer