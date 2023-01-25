function solution(array, commands) {
    let returnArr = [];
    for (let idx = 0; idx < commands.length; idx++) {
        let i = commands[idx][0];
        let j = commands[idx][1];
        let k = commands[idx][2];
        
        let answer = [...array].slice(i-1, j).sort((a,b) => (a-b));
        returnArr.push(answer[k-1])
    }
    return returnArr;
}