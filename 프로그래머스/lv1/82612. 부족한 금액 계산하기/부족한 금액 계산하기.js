function solution(price, money, count) {
    // 원래 이용료 : price 원
    // N번째 이용하면 : 이용료 * N
    
    for (let i = 1; i <= count; i++) {
        money -= price * i;
    }
    return money >= 0 ? 0 : -money;
}