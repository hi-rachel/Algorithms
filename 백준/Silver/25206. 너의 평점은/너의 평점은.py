grade_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
scores_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

sum = 0
major = 0

for n in range(20):
  name, scores, grade = input().split()
  scores = float(scores)
  
  if grade == 'P':
    continue;
  major += scores * scores_list[grade_list.index(grade)]
  sum += scores

if sum != 0:
  mean = major / sum
else:
  mean = 0
  
print(format(mean, '.6f'))