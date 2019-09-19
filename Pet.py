scores: int = []
sums = []
record = 0
winner = 0
for i in range(5):
    numbers = input().split()
    for k in range(4):
        numbers[k] = int(numbers[k])
    scores.append(numbers)
for j in range(5):
    sum_j = sum(scores[j])
    sums.append(sum_j)
for l in range(5):
    if sums[l] > record:
        record = sums[l]
        winner = l+1
print(winner, record)