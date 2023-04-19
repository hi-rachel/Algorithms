function solution(numbers) {
    let ans = new Array(numbers.length).fill(-1);
    let stack = [];
    for(let i = 0; i < numbers.length; i++){
        while(stack && numbers[stack.at(-1)] < numbers[i]){
            ans[stack.pop()] = numbers[i];
        }
        stack.push(i);
    }
    return ans;
}