allowance = int(input())
months = int(input())
left = 0

for i in range(months):
    used = int(input())
    left = allowance - used + left

print(left+allowance)