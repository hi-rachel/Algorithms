function solution(phone_book) {
    const hash_map = {}
    
    for (let phone of phone_book) {
        hash_map[phone] = 1
    }
    
    for (let phone of phone_book) {
        let arr = '';
        for (let num of phone) {
            arr += num;
            
            if (arr in hash_map && arr !== phone) {
                return false
            }
        }
    }
    return true 
}