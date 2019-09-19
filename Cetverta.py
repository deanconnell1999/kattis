x = []
y = []
for i in range(3):
    point = input().split()
    x.append(point[0])
    y.append(point[1])
x.sort()
y.sort()
for a in range(len(x)):
    if x[a] == x[a+1]:
        x.remove(x[a])
        x.remove(x[a])
        break
for b in range(len(y)):
    if y[b] == y[b+1]:
        y.remove(y[b])
        y.remove(y[b])
        break

print(x[0], y[0])