seznam = []
cisla = (input('Vložte čísla  a mezi nimi čárky:'))
seznam.append(cisla)
počet = 0
součet = 0
for i in seznam:
    počet+=1
    součet=i
print(sum(seznam))
print(součet/počet)



