function solution(rsp) {
    const rspOrder = rsp.split('');
    let result = [];
    for (let i = 0; i < rsp.length; i++) {
        if (rspOrder[i] === '0') {
            result.push('5');
        }
        if (rspOrder[i] === '2') {
            result.push('0');
        }
        if (rspOrder[i] === '5') {
            result.push('2')
        }
    }
    return result.join('');
    
}