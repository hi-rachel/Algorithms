function solution(balls, share) {
    let ballsFactorial = 1;
    let shareFactorial = 1;
    let availableFactorial = 1;
    
    for (let i = 1; i <= balls; i++) {
        ballsFactorial *= i;
    }
    for (let i = 1; i <= share; i++) {
        shareFactorial *= i;
    }
    for (let i = 1; i <= balls - share; i++) {
        availableFactorial *= i;
    }
    if (balls === share) {
        return 1;
    } else {
        return Math.round(ballsFactorial / (availableFactorial * shareFactorial));
    }
}