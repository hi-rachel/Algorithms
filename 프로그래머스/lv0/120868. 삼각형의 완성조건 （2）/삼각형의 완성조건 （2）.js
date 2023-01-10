function solution(sides) {
    let result = [];
    let max = sides.sort((a,b) => b-a)[0];
    let rest = sides.sort((a,b) => b-a)[1];
  
    for (let i = 1; i <= max; i++) {
        if (i + rest > max) {
            result.push(i);
        }
    }
  
  	for (let i = max + 1; i < max + rest; i++) {
      if (i < max+rest) {
      	result.push(i);
      }
    }
    return result.length;
}