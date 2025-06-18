/*
 * TC: O(N)
 * SC: O(N)
*/


function solution(s){
    const stack = []

    for (const char of s) {
        if (char === '(') {
            stack.push(char)
        } else {
            // 닫는 괄호가 나왔을 때 stack이 비어 있으면 false
            if (stack.length === 0) return false
            stack.pop()
        }
    }
    return stack.length === 0
}
