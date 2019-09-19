x = int(input())
for i in range(x):
    product = 1
    y = int(input())
    while y > 0:
        product = product * y
        y = y-1
    print(product%10)