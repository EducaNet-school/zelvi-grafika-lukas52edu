sez = []
firstnum = int(input("Zadejte prví číslo: "))
secondnum = int(input("Zadejte druhé číslo: "))

for num in range(firstnum,secondnum+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            sez.append(num)

print(sez)


