from math import sqrt, pow

x = input().split()
y = (int(x[0])+int(x[1])+int(x[2])+int(x[3]))/2
biggest = sqrt((y-int(x[0]))*(y-int(x[1]))*(y-int(x[2]))*(y-int(x[3])))
print(biggest)