function solution(s){
    const pRegex = /p/gi;
    const yRegex = /y/gi;
    let pCount = 0;
    let yCount = 0;
    
    if (s.includes('p') | s.includes('P')) {
        pCount = s.match(pRegex).length;
    }
    if (s.includes('y') | s.includes('Y')) {
        yCount = s.match(yRegex).length;
    }
    return pCount === yCount ? true : false;
}