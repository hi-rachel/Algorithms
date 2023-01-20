function solution(s) {
    let sArr = s.split('');
    let mid = Math.ceil(sArr.length / 2) - 1;
    return sArr.length % 2 == 0 ? sArr[mid]+sArr[mid+1] : sArr[mid];
}