function solution(phone_number) {
    let endNumber = [...phone_number].splice(-4).join('');
    phone_number = phone_number.replace(endNumber, '')
    const star = phone_number.replace(/\d/g, '*');
    return star+endNumber;   
}