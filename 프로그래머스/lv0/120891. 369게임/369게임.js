function solution(order) {
    let clap = 0;
    const game = ['3', '6', '9'];
    const orderList = order.toString().split('');
    for (let num of orderList) {
        if (game.some(n => num.includes(n))) {
            clap++;
        }
    }
    return clap;

}