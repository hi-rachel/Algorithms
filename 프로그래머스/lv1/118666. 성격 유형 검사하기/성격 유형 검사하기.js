function solution(survey, choices) {
    let result = '';
    
    let scores = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    
    for(let i = 0; i < choices.length; i++){
        if(choices[i] < 4) {
            scores[survey[i].split('')[0]] += Math.abs(choices[i] - 4);
        } else if (choices[i] > 4) {
            scores[survey[i].split('')[1]] += Math.abs(choices[i] - 4);
        } 
    }
    
    function higher(type1, type2){
        let set = '';
        set += scores[type1] >= scores[type2] ? type1 : type2;
        return set;
    }
    
    result += higher('R', 'T');
    result += higher('C', 'F');
    result += higher('J', 'M');
    result += higher('A', 'N');
    return result;
}