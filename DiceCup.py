dice = input().split()
record = 0
highest_tot = int(dice[0]) + int(dice[1])
tally = [0]*(highest_tot + 1)
for a in range(1, int(dice[0])+1):
	for b in range(1, int(dice[1])+1):
		temp = a + b
		tally[temp] = int(tally[temp]) + 1
		if tally[temp]>record:
			record = tally[temp]
for c in range(len(tally)):
	if tally[c] == record:
		print(c)