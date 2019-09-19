n = int(input())
ans = []
answer = []
for i in range(n):
    days = input().split()
    for j in range(int(days[0]), int(days[1])+1, 1):
        ans.append(j)
for a in ans:
    if a not in answer:
        answer.append(a)
print(len(answer))