function solution(num, total) {
    let start = Math.ceil(total / num - Math.floor(num / 2));
        
    return Array.from({length: num}, (_, i) => i + start);
}