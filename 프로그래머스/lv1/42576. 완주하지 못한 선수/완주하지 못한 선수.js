function solution(participant, completion) {
    participant = participant.sort();
    completion = completion.sort();
    let fail = [];
    for (let i = 0; i < participant.length; i++) {
        if (participant[i] !== completion[i]) {
            fail.push(participant[i]);
            participant.splice(i, 1);
        }
    }
    return fail.join();
}