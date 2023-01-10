function solution(my_string) {
    const result = my_string.match(/[0-9]+/g);
  	return result ? result.reduce((acc, cur) => acc + Number(cur), 0) : 0;
}
