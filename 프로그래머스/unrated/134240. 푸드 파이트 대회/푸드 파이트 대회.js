function solution(food) {
    let result ='';
    for (let i = 1; i < food.length; i++) {
        result += `${i}`.repeat(Math.floor(food[i]/2))
    }
    result += '0' + [...result].reverse().join('');
    return result;
}