term = int(input())
count = 0
current = 2
while count < term:
    current = 2*current - 1
    resultant = pow(current, 2)
    count = count + 1
print(int(resultant))