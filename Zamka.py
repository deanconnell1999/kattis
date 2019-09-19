lower = int(input())
upper = int(input())
win = int(input())
winners = []

for i in range(lower, upper+1, 1):
    total = 0
    str(i)
    for a in str(i):
        total += int(a)
    if total == win:
        winners.append(int(i))

winners.sort()

print(winners[0])
print(winners[-1])