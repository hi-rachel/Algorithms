function solution(ingredient) {
    let cnt = 0;
    for(let i = 0; i < ingredient.length; i++){
        if(ingredient.slice(i, i + 4).join('') == '1231'){
            cnt++;
            ingredient.splice(i, 4);
            i -= 3;
        };
    }
    return cnt;
}