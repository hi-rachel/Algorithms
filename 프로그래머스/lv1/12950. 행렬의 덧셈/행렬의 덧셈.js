function solution(arr1, arr2) {
    return arr1.map((list1, list2) => list1.map((num, idx) => num + arr2[list2][idx]));
}