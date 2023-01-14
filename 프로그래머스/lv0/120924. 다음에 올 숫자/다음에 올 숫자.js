function solution(common) {
    let result = 0;
    for (let i = 0; i < common.length; i++) {
        if (common[i+2] - common[i+1] == common[i+1] - common[i]) {
            result = common[common.length-1] + (common[i+1] - common[i]);
            return result;
        } else {
            result = common[common.length-1] * (common[i+1] / common[i]);
            return result;
        }
    }
}