n = input().split()
nums = [int(i) for i in n]
order = input()
nums.sort()
ans = ""
for a in range(3):
	if order[a] == "A":
		ans = ans + str(nums[0]) + " "
	if order[a] == "B":
		ans = ans + str(nums[1]) + " "
	if order[a] == "C":
		ans = ans + str(nums[2]) + " "
print(ans)