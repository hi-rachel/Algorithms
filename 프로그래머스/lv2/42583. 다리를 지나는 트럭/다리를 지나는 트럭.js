function solution(bridge_length, weight, truck_weights) {
    let cnt = 0;
    let queue = Array.from({length: bridge_length}, () => 0);
    let sum = 0;
    
    cnt++;
    queue.shift();
    sum += truck_weights[0];
    queue.push(truck_weights.shift());
    
    while(sum > 0){
        cnt++;
        sum -= queue.shift();
        if(truck_weights.length > 0 && sum + truck_weights[0] <= weight){
            sum += truck_weights[0];
            queue.push(truck_weights.shift());
        }else {
            queue.push(0);
        }
    }
    return cnt;
}