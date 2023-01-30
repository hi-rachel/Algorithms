function solution(s, n) {
    const LOWERCASE = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
    const UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = '';
    let sArr = s.split('');
    
    for (let i = 0; i <= sArr.length; i++) {
        if (sArr[i] == ' ') result += ' ';
        if (LOWERCASE.includes(sArr[i])) {
            let addIndex = LOWERCASE.indexOf(sArr[i]);
            result += LOWERCASE[addIndex+n]
    }
        if (UPPERCASE.includes(sArr[i])) {
            let addIndex = UPPERCASE.indexOf(sArr[i]);
            result += UPPERCASE[addIndex+n]
        }
    }
    return result;
}