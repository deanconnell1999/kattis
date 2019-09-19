from math import sqrt, pow

no_inputs = int(input())
sum = 0
for i in range(no_inputs):
    x = input()
    length = len(x)
    power = x[length-1]
    number = x[:length-1]
    actual = pow(int(number), int(power))
    sum += actual

print(int(sum))