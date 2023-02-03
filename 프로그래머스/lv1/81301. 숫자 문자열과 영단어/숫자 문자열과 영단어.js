function solution(s) {
    const englishDict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    while(Number.isNaN(+s) === true) {
        for (let key in englishDict) {
            s = s.replace(englishDict[key], key);
        }
    }
    return +s;
}