inp = input().split()
x = int(inp[0])
y = int(inp[1])
n = int(inp[2])
for i in range(1, n+1, 1):
    if i%x==0 and i%y==0:
        print("FizzBuzz")
        continue
    elif i%x==0 and i%y!=0:
        print("Fizz")
    elif i%x!=0 and i%y==0:
        print("Buzz")
    else:
        print(i)