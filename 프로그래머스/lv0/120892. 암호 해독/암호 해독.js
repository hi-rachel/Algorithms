function solution(cipher, code) {
    let result = '';
    const cipherArray = cipher.split('');
    for (let i = 1; i <= cipherArray.length / code; i++) {
        result += cipherArray[i * code - 1]; 
    }
    return result;
}