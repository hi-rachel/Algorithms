function solution(num_list) {
    let cnt = 0;
    num_list.forEach((num) => {
        while(num != 1){
             if(num % 2 != 0){
                num -= 1;
                } else {
                    num = num / 2;
                    cnt++;
                }
            }
    })
    return cnt;
}