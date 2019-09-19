from fileinput import input

for line in input():
    i = line.split()
    print(abs(int(i[0])-int(i[1])))