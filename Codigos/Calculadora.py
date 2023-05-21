while True:
    try:
        n1 = int(input("¿Dime el primer número?"))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")
while True:
    try:
        n2=int(input("¿Dime el segundo numero número?"))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")
suma=n1+n2
print("La suma de los dos numeros es: ", str(n1+n2) )
