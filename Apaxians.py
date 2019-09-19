fullname = input()
new = ""
for a in range(1, len(fullname)):
	if(not(fullname[a]==fullname[a-1])):
		new = new + fullname[a-1]
print(new+fullname[-1])