def solution(numbers, hand):
    result = ""
    left = "*"
    right = "#"
    
    def get_distance(located_num, target):
        keypad = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2],
            "*": [3, 0],
            0: [3, 1],
            "#": [3, 2],
        }
        
        now_position = keypad[located_num]
        target_position = keypad[target]
        
        return (
            abs(target_position[0] - now_position[0])
            + abs(target_position[1] - now_position[1])
        )
        
    for num in numbers:
        if((num == 1) or (num == 4) or (num == 7)):
            result += "L"
            left = num
        elif((num == 3) or (num == 6) or (num == 9)):
            result += "R"
            right = num
        else:
            left_distance = get_distance(left, num)
            right_distance = get_distance(right, num)
            
            if(left_distance < right_distance):
                result += "L"
                left = num
            elif(left_distance == right_distance):
                if hand == "left":
                    result += "L"
                    left = num
                else:
                    result += "R"
                    right = num
            else:
                result += "R"
                right = num
                
    return result