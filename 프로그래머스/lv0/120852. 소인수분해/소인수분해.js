function solution(n) {
    let answer = new Set();
    while (n % 2 == 0) {
        answer.add(2);
        n = n/2
    }

    for (var i = 3; i * i <= n; i += 2) {
        while (n % i === 0) {
            answer.add(i);
            n = n/i
        }
    }
    
    if (n > 2) {
        answer.add(n);
        return Array.from(answer);
    }
    
    return Array.from(answer);
}

