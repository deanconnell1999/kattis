cases = int(input())
temps = input().split()
x = 0
for i in range(len(temps)):
    if int(temps[i])<0:
        x = x+1
print(x)