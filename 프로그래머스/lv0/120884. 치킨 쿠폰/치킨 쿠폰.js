function solution(chicken) {
    let serviceChicken = 0;
    let coupon = chicken;
    while(coupon >= 10) {
        serviceChicken += Math.floor(coupon / 10);
        coupon = coupon % 10 + Math.floor(coupon / 10);
    }
    return serviceChicken;
}