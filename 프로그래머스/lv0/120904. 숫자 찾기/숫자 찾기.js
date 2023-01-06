function solution(num, k) {
    let numArr = num.toString().split('');
    for (let i = 0; i < numArr.length; i++) {
      if (+numArr[i] === k) {
        return numArr.indexOf(numArr[i])+1;
      }
    }
  	return -1;
}