function solution(nums) {
    let sorted = [...(new Set(nums))].sort();
    return sorted.length >= (nums.length / 2) ? (nums.length / 2) : sorted.length;
}