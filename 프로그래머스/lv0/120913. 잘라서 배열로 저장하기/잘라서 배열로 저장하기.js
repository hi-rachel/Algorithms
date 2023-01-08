function solution(my_str, n) {
    let result = [];
    let strArr = my_str.split('');
    while(strArr.length > 0) {
        result.push(strArr.splice(0, n).join(''));
    }
    return result;
}