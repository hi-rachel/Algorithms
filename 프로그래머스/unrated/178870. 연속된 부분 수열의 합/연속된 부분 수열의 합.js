function solution(sequence, k) {
    let result = [];
    let sum = 0;
    let l = 0;
    let idx = -1;
    
    while(true){
        if(sum < k){
            idx += 1
            if(idx >= sequence.length) break;
            sum += sequence[idx];
        } else {
            sum -= sequence[l];
            if(l >= sequence.length) break;
            l += 1;
        }
        if(sum == k) {
            result.push([l, idx]);
        }
    }
    result.sort((a, b) => (a[1] - a[0]) - (b[1] - b[0]));
    return result[0];
}