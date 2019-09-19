word = input()
word_array = []
per_array = []
count = 0
length = 0
for a in word:
    word_array.append(a)
    length = len(word_array)
for b in range(int(length/3)):
    per_array.append("P")
    per_array.append("E")
    per_array.append("R")
for c in range(length):
    if word_array[c] != per_array[c]:
        count = count + 1
print(count)