function solution(players, callings) {
    const mp = {};
    for(let i = 0; i < players.length; i++){
        mp[players[i]] = i; 
    }
    for(let i = 0; i < callings.length; i++){
        let idx = mp[callings[i]];
        let temp = players[idx-1];
        players[idx-1] = callings[i];
        players[idx] = temp;
        
        mp[callings[i]] = idx - 1;
        mp[temp] = idx;
    }
    return players;
}