while True:
	temp = 0
	num = int(input())
	if num == -1:
		exit()
	else:
		tot = 0
		for a in range(num):
			case = input().split()
			subtot = (int(case[0]))*(int(case[1])-temp)
			temp = int(case[1])
			tot = tot + subtot
		print(str(tot) + " miles")