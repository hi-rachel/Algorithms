function solution(participant, completion) {
    const checkMap = new Map();
    
    for (const name of completion) {
        checkMap.set(name, (checkMap.get(name) ?? 0) + 1)
    }
    for (const name of participant) {
        if (!checkMap.has(name) || checkMap.get(name) <= 0) {
            return name
        } else {
            checkMap.set(name, checkMap.get(name) - 1)
        }
    }
}