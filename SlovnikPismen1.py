retezec1 = input("Zadej slovo: ").lower()
slovnik1 = {}

for retezec1 in retezec1:
    if retezec1 in slovnik1:
        slovnik1[retezec1] += 1
    else:
        slovnik1[retezec1] = 1

print(slovnik1)
