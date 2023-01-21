function solution(s) {
    // ABDCEFvr -> vrFEDCBA
    let upper = s.match(/[A-Z]/g);
    if (upper) {
        for (let i = 0; i < upper.length; i++) {
            s = s.replace(upper[i], '');
        }
        return Array.from(s).sort().reverse().join('') + upper.sort().reverse().join('');
    } else {
        return Array.from(s).sort().reverse().join('');
    }   
}