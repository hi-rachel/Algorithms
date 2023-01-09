function solution(keyinput, board) {
    let x = 0;
    let y = 0;
    let result = [];
    for (let i = 0; i < keyinput.length; i++) {
        if (Math.abs(x) < Math.floor(board[0]/2)) {
            if (keyinput[i] === "left") {
                x -= 1;
            }
            if (keyinput[i] === "right") {
                x += 1;
            }
        }
        
        if (Math.abs(y) < Math.floor(board[1]/2)) {
            if (keyinput[i] === "up") {
                y += 1;
            }
            if (keyinput[i] === "down") {
                y -= 1;
            }
        }

    }
    return result.concat([x,y]);
}