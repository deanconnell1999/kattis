c = float(input())
l = int(input())
sum = 0
for i in range(l):
    d = input().split()
    sum = sum + (float(d[0])*float(d[1])*c)
print(sum)