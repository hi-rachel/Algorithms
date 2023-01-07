function solution(str1, str2) {
    return str1.split(str2).length >= 2 ? 1 : 2;
}