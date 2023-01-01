function solution(my_string) {
    let num = my_string.match(/\d/g);
    return num.map(x=>+x).reduce((a,b) => (a+b));
}