function solution(s) {
    const sortS = s.split(' ').sort((a, b) => a-b);
    const min = sortS[0];
    const max = sortS[sortS.length-1];
    return `${min} ${max}`;
}