function solution(a, b, n) {
    let result = 0;
    while (n >= a) {
        let emptyBottle = Math.floor(n / a) * a;
        let newCoke = Math.floor(n / a) * b;
        result += newCoke;
        n += newCoke - emptyBottle;
    }
    return result;
}