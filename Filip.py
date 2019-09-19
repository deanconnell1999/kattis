numbers = input().split()
numbers[0] = numbers[0][::-1]
numbers[1] = numbers[1][::-1]
print(max(numbers))