assets = input().split()
gold = int(assets[0])
silver = int(assets[1])
copper = int(assets[2])

money = gold*3 + silver*2 + copper*1

if 8 <= money:
    print("Province or Gold")
elif 6 <= money < 8:
    print("Duchy or Gold")
elif 5 == money:
    print("Duchy or Silver")
elif 3 <= money < 5:
    print("Estate or Silver")
elif 2 == money:
    print("Estate or Copper")
else:
    print("Copper")