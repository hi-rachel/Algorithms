function solution(n, w, num) {
    // 상자의 위치를 찾기 위해 층과 해당 층에서의 위치 계산
    let layer = Math.floor((num - 1) / w) + 1; // 몇 번째 층인지
    let posInLayer = (num - 1) % w + 1; // 해당 층에서 몇 번째 위치인지

    // 지그재그 패턴 적용: 짝수 층은 오른쪽에서 왼쪽으로
    if (layer % 2 === 0) {
        posInLayer = w - posInLayer + 1;
    }

    // 위에 있는 상자의 수 계산
    let result = 0;
    
    // 전체 층 수 계산
    let totalLayers = Math.ceil(n / w);
    
    // 꺼내려는 상자의 윗층에 있는 모든 상자를 꺼내야 함
    for (let l = layer + 1; l <= totalLayers; l++) {
        // 남은 상자 수 계산 (마지막 층은 w개보다 적을 수 있음)
        let boxesInThisLayer = (l === totalLayers) ? (n - (l-1) * w) : w;
        
        // 윗층에 있는 모든 상자 중 열이 같은 상자만 꺼내야 함
        for (let p = 1; p <= boxesInThisLayer; p++) {
            // 지그재그 패턴에 따라 현재 위치 계산
            let currentPos = (l % 2 === 1) ? p : (w - p + 1);
            
            // 현재 상자가 꺼내려는 상자의 위에 있는지 확인
            if (currentPos === posInLayer) {
                result++;
            }
        }
    }
    
    // 꺼내려는 상자 자체도 포함
    result++;
    
    return result;
}