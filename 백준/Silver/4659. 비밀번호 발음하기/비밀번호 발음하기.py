vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def is_acceptable_password(password):
    has_vowel = False
    for vowel in vowels:
        if vowel in password:
            has_vowel = True
            break
    if not has_vowel:
        return False
    
    consecutive_vowels = 0
    consecutive_consonants = 0
        
    for char in password:
        if char in vowels:
            consecutive_vowels += 1
            consecutive_consonants = 0
        else:
            consecutive_consonants += 1
            consecutive_vowels = 0

        if consecutive_vowels >= 3 or consecutive_consonants >= 3:
            return False
        
    for i in range(0, len(password)-1):
        prev = password[i]
        next = password[i+1]
        if prev == next:
            if prev != 'e' and prev != 'o':
                return False
            
    return True

while True:
    test = str(input())
    
    if test == 'end':
        break

    if is_acceptable_password(test) == True:
        print('<' + test + '>' + ' is acceptable.')
    else:
        print('<' + test + '>' + ' is not acceptable.')