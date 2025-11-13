#comparacion de tres numeros
numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero:"))
numero3=int(input("ingrese el seundo numero:"))         
if numero1>numero2 and numero1>numero3:
    print("el numero mayor es:",numero1)
elif numero2>numero1 and numero2>numero3:
    print("el numero mayor es :",numero2)
else:
    print("el numero mayor es :",numero3)
