function solution(s, skip, index) {
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    
    for (let i = 0; i < skip.length; i++) {
        alphabet = alphabet.replace(skip[i], "");
    }

    let result = "";
    for (let i = 0; i < s.length; i++) {
        let idx = alphabet.indexOf(s[i])+index;
        
        while (alphabet.length <= idx) {
        idx = idx - alphabet.length;
        }
        
        result += alphabet[idx];
    }
    return result;
    }