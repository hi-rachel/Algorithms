function solution(A,B){
    let answer = [];
    let sortA = A.sort((a,b) => a-b);
    let sortB = B.sort((a,b) => b-a);
    for (let i = 0; i < A.length; i++) {
        answer.push(sortA[i] * sortB[i]);
    }
    return answer.reduce((acc, cur) => acc + cur, 0);
}