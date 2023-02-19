// function solution(k, tangerine) {
//     // 귤의 종류
//     const sorted = Array.from(new Set(tangerine));

//     // 종류별 개수 구하기
//     let count = new Array(sorted.length).fill(0);
//     let box = [];
 
//     while (tangerine.length > 0) {
//         for (let i = 0; i < sorted.length; i++) {
//             if (tangerine.includes(sorted[i])) {
//                 count[i]++;
//                 let idx = tangerine.indexOf(sorted[i]);
//                 tangerine.splice(idx, 1);
//             }
//         }
//     }
    
//     // 가장 많은 개수를 가지고 있는 종류부터 k개 만큼 상자에 담기
//     while (box.length !== k) {
//         let maxIdx = count.indexOf(Math.max.apply(null, count));
//         count.splice(maxIdx, 1);
//         box.push(sorted[maxIdx]);
//         k--;
//         sorted.splice(maxIdx, 1);
//     }
//     return box.length;
// }

function solution(k, tangerine) {
  let answer = 0;
    
  // 귤 객체를 초기화
  const tDict = {};

  // 값만을 도출하여 내림차순으로 정렬해 줍니다 - 키는 모두 다르기에
  tangerine.forEach((t) => tDict[t] = (tDict[t] || 0) + 1);
    
  const tArr = Object.values(tDict).sort((a, b) => b - a);
    
  // 필요한 귤만큼 가짓수를 더해줍니다
  for (const t of tArr) {
    answer++;
    if (k > t) k -= t;
    else break;
  }
  return answer;
}