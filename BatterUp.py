denom = int(input())
score = input().split()
num = 0
for i in range(len(score)):
    if score[i] == "-1":
        denom = denom - 1
    else:
        num = num + int(score[i])
print(num/denom)