function solution(num) {
    let collatzCount = 0;
    
    if (num === 1) {
        return 0;
    } else {
        while (num != 1) {
            num % 2 === 0 ? num = num / 2 : num = num * 3 + 1;
            collatzCount +=1;
        }
        return collatzCount < 500 ? collatzCount : -1;
    }
}