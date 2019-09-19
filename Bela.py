inp = input().split()
hands = int(inp[0])
dom = inp[1]
tot = 0
for i in range(4 * hands):
    card = input()
    num = card[0]
    suit = card[1]
    if num == "J" and suit == dom:
        tot = tot + 20
    elif num == "9" and suit == dom:
        tot = tot + 14
    elif num == "A":
        tot = tot + 11
    elif num == "K":
        tot = tot + 4
    elif num == "Q":
        tot = tot + 3
    elif num == "J" and suit != dom:
        tot = tot + 2
    elif num == "T":
        tot = tot + 10
    else:
        tot = tot + 0
print(tot)