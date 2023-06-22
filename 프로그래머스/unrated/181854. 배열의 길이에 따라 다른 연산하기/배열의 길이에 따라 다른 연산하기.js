function solution(arr, n) {
    for(let i = 0; i < arr.length; i++){
        if(arr.length % 2 == 0){
            if(i % 2 != 0) arr[i] += n;
        } else {
            if(i % 2 == 0) arr[i] += n;
        }
    }
    return arr;
}