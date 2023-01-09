function solution(numbers) {
    const sorting = numbers.sort((a, b) => b - a);
    if (sorting[0] * sorting[1] > sorting[numbers.length-1] * sorting[numbers.length-2]) {
        return sorting[0] * sorting[1];
    } else {
        return sorting[numbers.length-1] * sorting[numbers.length-2];
    }
}