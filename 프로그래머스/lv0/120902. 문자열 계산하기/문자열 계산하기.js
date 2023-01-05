function calculate(fn) {
    return new Function('return ' + fn)();
}
function solution(my_string) {
    return calculate(my_string);
}