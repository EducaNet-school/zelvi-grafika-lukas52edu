number = int(input("Zadejte číslo: "))

if number % 2 == 0:
    number += 1
    list = [number]
for i in range(9):
    number += 2
    list.append(number)
print(list)

