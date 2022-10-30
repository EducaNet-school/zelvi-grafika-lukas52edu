print("Vypíši ti Fibonacciho posloupnost. \n")
konec = int(input("Jaká bude limitní hodnota: "))
a = 0
b = 1
řadek=0
while b<=konec:
    print(a, " ",
    end="" )
    print(b, " ",
    end="" )
    a=a+b
    b=b+a
    řadek+=1
    if řadek%5==0:
        print("\n")
if a<=konec:
    print(a)
