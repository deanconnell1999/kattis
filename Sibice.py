from math import sqrt, pow

line1 = input().split()
no_matches = int(line1[0])
diagonal = sqrt(pow(int(line1[1]), 2)+pow(int(line1[2]), 2))

for i in range(no_matches):
    number = int(input())
    if number > diagonal:
        print("NE")
    else:
        print("DA")