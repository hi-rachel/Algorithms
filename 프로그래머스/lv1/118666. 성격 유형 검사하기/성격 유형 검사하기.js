function solution(survey, choices) {
    let result = '';
    
    let scores = {
        // 1번 지표
        'R': 0,
        'T': 0,
        // 2번 지표
        'C': 0,
        'F': 0,
       // 3번 지표
        'J': 0,
        'M': 0,
        // 4번 지표
        'A': 0,
        'N': 0,
    }
    
    for(let i = 0; i < choices.length; i++){
        if(choices[i] < 4) {
            // 비동의
            scores[survey[i].split('')[0]] += Math.abs(choices[i] - 4);
        } else if (choices[i] > 4) {
            // 동의
            scores[survey[i].split('')[1]] += Math.abs(choices[i] - 4);
        } 
    }
    function higher(type1, type2){
        let set = '';
        if(scores[type1] > scores[type2]) {
            set += type1;
        } else if(scores[type1] == scores[type2]){
            set += (type1 > type2 ? type2 : type1);
        } else {
            set += type2;
        }
        return set;
    }
    result += higher('R', 'T');
    result += higher('C', 'F');
    result += higher('J', 'M');
    result += higher('A', 'N');
    return result;
}