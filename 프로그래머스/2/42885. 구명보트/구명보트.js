// TC: O(N log N), SC: O(1)

function solution(people, limit) {
    people.sort((a, b) => a - b);
    let i = 0, j = people.length - 1;
    
    while (i < j) {
        if (people[i] + people[j] <= limit) {
            i++; // limit 안넘으면 가장 가벼운 사람 같이 태움
        }
        j--; // 제일 무거운 사람 탑승
    }

    return people.length - i;
}