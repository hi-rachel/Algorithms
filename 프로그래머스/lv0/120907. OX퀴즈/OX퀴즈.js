function solution(quiz) {
    let result = [];
    for (let study of quiz) {
      let problem = study.split('=');
      let solve = eval(problem[0]);
      let answer = +problem[1];
        solve === answer ? result.push("O") : result.push("X");
    }
    return result;
}