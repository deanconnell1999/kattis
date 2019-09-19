testcases = int(input())
for a in range(testcases):
	num = int(input())
	cities = set()
	for b in range(num):
		city = input()
		if city not in cities:
			cities.add(city)
	print(len(cities))