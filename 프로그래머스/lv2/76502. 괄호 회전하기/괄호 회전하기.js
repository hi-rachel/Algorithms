function solution(s) {
    let answer = 0;
    
    const sLen = s.length;
    for (let i = 0; i < sLen; i++) {
        const stack = [];
        s.split('').forEach((v) => {
            if (stack.length === 0) stack.push(v);
            else if (v === ")" && stack[stack.length - 1] === "(") stack.pop();
            else if (v === "}" && stack[stack.length - 1] === "{") stack.pop();
            else if (v === "]" && stack[stack.length - 1] === "[") stack.pop();
            else stack.push(v);
        });
        
        if (stack.length === 0) answer++;
        
        s = s.split('').map((v, i, arr) => arr[(i+1) % sLen]).join('');
    }
    return answer;
}