function solution(n, m) {
    function range(min, max) {
        let arr = [];
        for (let i = min; i <= max; i++) {
            arr.push(i);
        }
        return arr;
    }
    
    // 최대공약수 : the greatest common denominator(GCD)
    function gcd(a, b) {
        return !b ? a : gcd(b, a % b);
    }
    
    
    // 최소공배수 : the least common multiple(LCM)
    function lcm(a,b) {
        return (a * b) / gcd(a, b);
    }
    
    return [gcd(n, m), lcm(n,m)];
}