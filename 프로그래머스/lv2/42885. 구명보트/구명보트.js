function solution(people, limit) {
   let sorted = people.sort((a,b) => a-b);
    let i, j = 0;
    for (i = 0, j = sorted.length-1; i < j; j--) {
        if (sorted[i] + sorted[j] <= limit) i++;
    }
    return sorted.length - i;
}