n=int(input("Ingrese un numero: "))
if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n, "es un numero impar")

for i in range (2,n):
    if n % i == 0:
        print("El numero no es primo")
    else:
        print("El numero es primo")

if n > 50 :
    print("El numero es mayor a 50")
else:
    print("El numero es menor a 50")
