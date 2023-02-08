function solution(nums) {
    const answer = [];
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            for (let k = j+1; k < nums.length; k++) {
                answer.push(nums[i] + nums[j] + nums[k]);
            }
        }
    }
    return answer.filter(i => isPrime(i)).length;
}

function isPrime(number) {
    if (number % 2 === 0) return false;
    for (let i = 3; i * i <= number; i += 2) {
        if (number % i === 0) return false;
    }
    return true;
}