function solution(age) {
    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
    let eachAge = String(age).split('');
    let result = '';
    for (let i = 0; i<eachAge.length; i++) {
        const index = Number(eachAge[i]);
        result += alphabet[index];
    }
    return result;
}