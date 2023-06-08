function solution(park, routes) {
    // 직사각형 공원의 가로, 세로 길이
    // 가로 Row => 셀 때는 세로 방향으로 센다.
    const maxRow = park.length - 1;
    // 세로 Column => 셀 때는 가로 방향으로 센다.
    const maxCol = park[0].length - 1;
    
    // 시작 지점의 좌표 
    let row = park.findIndex((s) => s.includes("S"));
    let col = park[row].indexOf("S");
    
    // routes 각 요소 하나씩 확인
    routes.forEach((position) => {
        // 구조분해할당, 요소를 빈칸 기준으로 나눠줌.
        // [direction, number]
        const [d, n] = position.split(' ');
        
        // 임시 좌표
        let tempRow = row;
        let tempCol = col;
        let flag = true;
        
        for(let i = 0; i < Number(n); i++){
            // 동쪽(E) Col++ / 남쪽(S) Row++
            // 서쪽(W) Col-- / 북쪽(N) Row--
            if(d === "E") tempCol++;
            else if(d === "W") tempCol--;
            else if(d === "S") tempRow++;
            else if(d === "N") tempRow--;
            
            if(
                // 행(가로)과 열(세로)가 공원에서 벗어나는지
                tempRow > maxRow ||
                tempRow < 0 ||
                tempCol > maxCol ||
                tempCol < 0 ||
                // 장애물은 없는지 확인
                park[tempRow][tempCol] === "X"
            ) {
                // 벗어나거나 장애물이 있다면
                flag = false;
                // for문 종료
                break;
            }
        }
        // 통과했다면 이동한 것이므로 실제 좌표에 임시 좌표 대입
        if(flag){
            col = tempCol;
            row = tempRow;
        }
    });
    return [row, col];
}