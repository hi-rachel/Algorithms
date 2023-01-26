function solution(d, budget) {
    let count = 0;
    let sorted = d.sort((a,b) => (a-b));

    for (let n of sorted) {
        budget -= n
        if (budget < 0) break;
        count++;
    }
    return count;
}