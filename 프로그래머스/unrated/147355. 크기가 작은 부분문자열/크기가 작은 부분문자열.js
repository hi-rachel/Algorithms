function solution(t, p) {
  const setLength = p.length;
  let numList = [];
  for (let i = 0; i < t.length; i++) {
    numList.push([...t].slice(i, i + setLength).join(''));
  }
  numList = numList.filter(x => x.length === setLength);
  let count = 0;
  numList.map(x => (+x <= +p ? count++ : null));
  return count;
}