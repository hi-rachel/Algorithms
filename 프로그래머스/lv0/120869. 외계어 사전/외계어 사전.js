function solution(spell, dic) {
  return dic.some(s => Array.from(s).sort().join('').includes(spell.sort().join(''))) ? 1 : 2;
	
}