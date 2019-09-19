time = input().split()
hours = int(time[0])
minutes = int(time[1])

if minutes >= 45:
    print(hours, (minutes-45))
else:
    if hours == 0:
        hours = 24
    print(hours-1, (minutes-45) % 60)