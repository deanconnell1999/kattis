start = input()
while True:
    tot = 0
    for i in str(start):
        tot = tot + int(i)
    if int(start) % tot == 0:
        print(start)
        exit()
    else:
        start = int(start) + 1