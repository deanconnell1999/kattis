n = int(input())
for i in range(n):
    case = input().split()
    if int(case[0])>(int(case[1])-int(case[2])):
        print("do not advertise")
    elif int(case[0])<(int(case[1])-int(case[2])):
        print("advertise")
    else:
        print("does not matter")