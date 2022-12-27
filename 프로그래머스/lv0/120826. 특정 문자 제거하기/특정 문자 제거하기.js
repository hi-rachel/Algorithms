function solution(my_string, letter) {
    const regex = new RegExp(letter, 'g');
    my_string = my_string.replace(regex, '');
    return my_string;
}