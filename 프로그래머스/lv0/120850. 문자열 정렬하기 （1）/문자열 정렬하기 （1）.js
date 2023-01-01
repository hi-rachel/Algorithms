function solution(my_string) {
    let num = my_string.match(/\d/g);
    return num.sort().map(x =>+x);
}