while True:
	case = input().split()
	if (int(case[0])==0 and int(case[1])==0):
		exit()
	else:
		num = int(case[0])
		denom = int(case[1])
		floor = num//denom
		mod = num%denom
		print(str(floor) + " " + str(mod) + " / " + str(denom))
	