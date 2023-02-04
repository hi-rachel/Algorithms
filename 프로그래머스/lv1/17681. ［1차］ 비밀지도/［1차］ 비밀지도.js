function solution(n, arr1, arr2) {
    // 지도 1 또는 지도 2 중 어느 하나라도 벽! => 전체 지도에서도 벽(1)
    // 지도 1과 지도 2 모두! 공백 => 전체 지도에서도 공백(0)
    
    const map1 = arr1.map(x => x.toString(2).padStart(n, '0'));
    const map2 = arr2.map(x => x.toString(2).padStart(n, '0'));
    
    let result = [];
    for (let i = 0; i < map1.length; i++) {
        let test1 = map1[i].split('');
        let test2 = map2[i].split('');
        
        let testResult = '';
        for (let j = 0; j < test1.length; j++) {        
            test1[j] == 0 && test2[j] == 0 ? testResult += ' ' : testResult += '#';
        }
        result.push(testResult);
        testResult = '';
    }
    return result;
}