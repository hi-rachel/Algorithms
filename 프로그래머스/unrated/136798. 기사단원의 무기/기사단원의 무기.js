function solution(number, limit, power) {
    if(number == 1) return 1;
    let n = [];
    for(let i = 1; i <= number; i++){
        let c = 1;
        for(let j = 1; j <= i/2; j++){
            if(i % j === 0) c += 1;
        }
        if(c > limit) c = power;
        n.push(c);
    }
    return n.reduce((cur, acc) => cur + acc, 0);
}