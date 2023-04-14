function solution(name, yearning, photo) {
    let result = [];
    for(let i = 0; i < photo.length; i++){
        let test = photo[i];
        let ans = 0;
        for(let j = 0; j < test.length; j++){
            let idx = name.indexOf(test[j]);
            if(idx >= 0) ans += yearning[idx];
        }
        result.push(ans);
        ans = 0;
    }
    return result;
}