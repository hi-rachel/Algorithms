function solution(numbers, hand) {
    let left = "*";
    let right = "#";
    let result = "";
    
    const getDistance = (locatedNumber, target) => {
        const keyPad = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2],
            "*": [3, 0],
            0: [3, 1],
            "#": [3, 2],
        };
        
        const nowPosition = keyPad[locatedNumber];
        const targetPosition = keyPad[target];
        
        return (
            Math.abs(targetPosition[0] - nowPosition[0])
            + Math.abs(targetPosition[1] - nowPosition[1])
        );
    };
    
    for(let i = 0; i < numbers.length; i++) {
        if((numbers[i] == 1) || (numbers[i] == 4) || (numbers[i] == 7)){
            result += "L";
            left = numbers[i];
        } else if((numbers[i] == 3) || (numbers[i] == 6) || (numbers[i] == 9)) {
            result += "R"
            right = numbers[i];
        } else {
            let leftDistance = getDistance(left, numbers[i]);
            let rightDistance = getDistance(right, numbers[i]);

            if(leftDistance < rightDistance) {
                result += "L";
                left = numbers[i];
            } else if(leftDistance == rightDistance) {
                if(hand == "left") {
                    result += "L";
                    left = numbers[i];
                } else {
                    result += "R"
                    right = numbers[i];
                }
            } else {
                result += "R"
                right = numbers[i];
            }
        }
    }
    return result;
}