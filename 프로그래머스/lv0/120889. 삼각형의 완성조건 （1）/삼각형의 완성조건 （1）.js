function solution(sides) {
    const sortSides = sides.sort(function(a,b) {
        return a - b;
    });
    const max = sortSides.pop(sortSides[sortSides.length -1]);
    if (max < sortSides.reduce((a,b) => a+b)) {
        return 1;
    } else return 2;
}