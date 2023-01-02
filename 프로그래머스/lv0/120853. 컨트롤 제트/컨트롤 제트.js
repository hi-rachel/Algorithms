function solution(s) {
    const eachS = s.split(' ');
    
    let stack = [];
    
    for (let i = 0; i < eachS.length; i++) {
        if (eachS[i] !== "Z") {
            stack.push(eachS[i]);;
        } else {
            stack.pop();
        }
    }
    
    const sum = stack.reduce((acc, curr) => {
        return acc + Number(curr);
    }, 0);
    return sum;
}