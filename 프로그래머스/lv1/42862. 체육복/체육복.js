function solution(n, lost, reserve) {
    // 양쪽 순서 학생에게만 체육복을 빌려줄 수 있음
    // 전체 학생 수 n, 체육복 도난 학생 번호 lost, 여벌의 체육복 가져온 학생들 번호 reserve
    let students = [];
    for (let i = 1; i <= n; i++) {
        students.push(i);
    }
    
    // 도난 당한 학생 제외
    const haveClothes = students.filter((x => !lost.includes(x)));
    let count = haveClothes.length;
    
    // 체육복 빌려주기
    console.log(haveClothes);
    for (let j = 0; j < count; j++) {
        if (lost.includes(haveClothes[j] - 1)) {
            count++;
            lost.splice(j-1, 1)
        } else if (lost.includes(haveClothes[j] + 1)) {
            count++;
            lost.splice(j+1, 1)
        }
        // else {
        //     return count;
        // }
    }
    return count;
}