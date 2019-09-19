from math import sin, pi
inp = input().split()
h = int(inp[0])
v = int(inp[1])
v = v*(pi/180)
print(int(h/sin(v))+1)