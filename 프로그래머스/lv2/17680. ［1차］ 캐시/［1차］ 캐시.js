function solution(cacheSize, cities) {
    // DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성
    // 캐시 교체 알고리즘 => Least Recently Used 가장 최근에 사용한 캐시 교체
    
    let answer = 0;
    let cityArr = [];
    
    // cities의 각각 city 실행
    for (let i = 0; i < cities.length; i++) {
        let current = cities[i].toLowerCase();
        let findCity = cityArr.find((city) => city === current);
        // cityArr에 현재 city가 존재하지 않는다면 추가
        if (!findCity) {
            cityArr.push(current);
            // 캐시크기보다 커지면 맨 앞 캐시 삭제 => cache miss => 실행시간 + 5
            if (cityArr.length > cacheSize) {
                cityArr.shift();
            }
            answer += 5;
            // cityArr에 현재 city가 존재한다면 해당 city 제거 후 마지막에 city 넣어줌 => cache hit => 실행시간 + 1
        } else {
            cityArr = cityArr.filter((city) => city !== current);
            cityArr.push(current);
            answer++;
        }
    }
    return answer;
}