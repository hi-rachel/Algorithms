function solution(cacheSize, cities) {
    // DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성
    // 캐시 교체 알고리즘 => Least Recently Used 가장 최근에 사용한 캐시 교체
    
    let answer = 0;
    let cityArr = [];
    
    for (let i = 0; i < cities.length; i++) {
        let current = cities[i].toLowerCase();
        let findCity = cityArr.find((city) => city === current);
        if (!findCity) {
            cityArr.push(current);
            if (cityArr.length > cacheSize) {
                cityArr.shift();
            }
            answer += 5;
        } else {
            cityArr = cityArr.filter((city) => city !== current);
            cityArr.push(current);
            answer++;
        }
    }
    return answer;
}