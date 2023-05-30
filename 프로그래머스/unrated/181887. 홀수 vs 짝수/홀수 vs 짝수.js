function solution(num_list) {
    let one = 0;
    let two = 0;
    for(let i = 0; i < num_list.length; i++){
        if(i == 0 || ((i+1) % 2 != 0)){
            one += num_list[i];
        } else {
            two += num_list[i];
        }
    }
    return one > two ? one : two;
}