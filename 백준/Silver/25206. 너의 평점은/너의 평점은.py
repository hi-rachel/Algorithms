sum = 0
major = 0

for n in range(20):
  name, scores, grade = input().split()
  scores = float(scores)
  if grade == 'P':
    continue;
  if grade == 'A+':
    major += 4.5 * scores
  if grade == 'A0':
    major += 4.0 * scores
  if grade == 'B+':
    major += 3.5 * scores
  if grade == 'B0':
    major += 3.0 * scores
  if grade == 'C+':
    major += 2.5 * scores
  if grade == 'C0':
    major += 2.0 * scores
  if grade == 'D+':
    major += 1.5 * scores
  if grade == 'D0':
    major += 1.0 * scores
  if grade == 'F':
    major += 0.0 * scores
  sum += scores

if sum != 0:
  mean = major / sum
else:
  mean = 0
  
print(format(mean, '.6f'))