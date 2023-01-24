function solution(arr)
{   
    let answer = [];
    arr.forEach((element, index, array) => {
        if (index === 0) answer.push(element);
        else if (array[index-1] !== element) {
            answer.push(element);
        }
    })
    return answer;
}