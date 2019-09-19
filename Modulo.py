distinct = set()
for a in range(10):
	temp = int(input())
	mod = temp % 42
	distinct.add(mod)
print(len(distinct))