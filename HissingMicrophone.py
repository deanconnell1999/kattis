word = input()
for i in range(len(word)-1):
    if word[i] == "s" and word[i+1] == "s":
        print('hiss')
        exit()
print("no hiss")