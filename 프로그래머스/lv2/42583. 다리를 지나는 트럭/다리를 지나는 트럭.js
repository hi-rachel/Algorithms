function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    // 가능한 다리에 올라갈 수 있는 트럭 수만큼 Array 0으로 채우기
    let queue = Array.from({length:bridge_length}, () => 0);
    let sum = 0;
    
    answer++;
    queue.shift();
    sum += truck_weights[0];
    queue.push(truck_weights.shift());
    
    while(sum > 0){
        answer++;
        sum -= queue.shift();
        if(truck_weights.length > 0 && weight >= sum + truck_weights[0]){
            sum += truck_weights[0];
            queue.push(truck_weights.shift());
        } else {
            queue.push(0);
        }
    }
    return answer;
}