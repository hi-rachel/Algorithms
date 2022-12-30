function solution(numbers, direction) {
    if (direction == "right") {
        let last = numbers.splice(numbers.length-1, 1);
      	return(last.concat(numbers));
    }
      if (direction == "left") {
        let first = numbers.splice(0, 1);
      	return(numbers.concat(first));
    }
}
