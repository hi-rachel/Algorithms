function solution(my_string, num1, num2) {
    const stringArray = my_string.split('');
    const stringArrayCopy = [...stringArray];
    stringArray[num1] = stringArrayCopy[num2];
    stringArray[num2] = stringArrayCopy[num1];
    return stringArray.join('');
}