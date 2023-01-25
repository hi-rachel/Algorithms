// function solution(numbers) {
//     // const answer = numbers.sort((a,b) => `${b}${a}` - `${a}${b}`);
//     const answer = numbers.sort((a,b) => `${a}${b}` - `${b}${a}`);
//     return answer[0] === 0 ? ""+answer[0] : answer.join('');
// }

function solution(numbers) {
    numbers.sort((a,b)=>{
        let sa = a.toString();
        let sb = b.toString();
        return parseInt(sa + sb) > parseInt(sb + sa) ? -1 : 1;
    })
    if(numbers[0] === 0) return '0'
    
    return numbers.join('')
};