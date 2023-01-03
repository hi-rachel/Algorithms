function solution(array, n) {
    const result = array.sort().map((x) => Math.abs(x-n));
  	const maxIndex = result.indexOf(Math.min.apply(Math, result));
  	return array.sort()[maxIndex];
  
}