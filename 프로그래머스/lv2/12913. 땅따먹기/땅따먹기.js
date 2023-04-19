function solution(land) {
    let ans = [];
    for(let i = 1; i < land.length; i++){
        let p = land[i -1];
        let c = land[i];
        c[0] += Math.max(
            p[1], p[2], p[3]
        );
        c[1] += Math.max(
            p[0], p[2], p[3]
        );
        c[2] += Math.max(
            p[0], p[1], p[3]
        )
        c[3] += Math.max(
            p[0], p[1], p[2]
        )
        ans = land[land.length-1];
    }
    return Math.max(...ans);
}