num = int(input())
for a in range(num):
	instruction = input()
	if instruction[0:10] == "Simon says":
		print(instruction[10:])