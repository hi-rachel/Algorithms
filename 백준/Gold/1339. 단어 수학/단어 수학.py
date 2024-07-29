N = int(input())
words = [input().strip() for _ in range(N)]

weight = {}

def calculateWeights(word):
    length = len(word)
    for i, char in enumerate(word):
        if char in weight:
            weight[char] += 10 ** (length - i - 1)
        else:
            weight[char] = 10 ** (length - i - 1)

for word in words:
    calculateWeights(word)

sorted_char = sorted(weight.items(), key=lambda x: x[1], reverse=True)

num_dict = {}
num = 9
for char, _ in sorted_char:
    num_dict[char] = num
    num -= 1

ans = 0
for word in words:
    nums_str = ''.join(str(num_dict[char]) for char in word)
    ans += int(nums_str)

print(ans)