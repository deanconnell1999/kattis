no = int(input())
junk = input().split()
record = 10000000000
for i in range(no):
    if int(junk[i]) < int(record):
        record = junk[i]
        day = i
print(day)