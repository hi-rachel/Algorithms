function solution(hp) {
    let top = Math.floor(hp / 5);
    let second = Math.floor((hp - top * 5) / 3);
    let third = Math.floor((hp - top * 5 - second * 3) / 1);
    return top + second + third;
}