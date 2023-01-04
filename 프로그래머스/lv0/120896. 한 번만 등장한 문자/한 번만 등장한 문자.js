function solution(s) {
    const arr = s.split('').sort();
  	let removeS = [];
    for (let i = arr.length; i >= 0; i--) {
        if (arr[i] === arr[i-1]) {
            removeS.push(arr[i]);
        }
      	if (removeS.some(n => arr[i].includes(n))) {
        		delete arr[i];
        }
    }
  	let onlyOne = arr.filter((element) => element !== undefined);
    return onlyOne.join('').toString();
}