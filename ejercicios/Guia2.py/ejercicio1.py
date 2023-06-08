def numeroaindicar(num01):
    numero=[]
    for _ in range(num01):
        numeros=int(input("ingrese un numero: "))
        numero.append(numeros)
    return numero

def sumas(numero):
    total= sum(numero)
    pares= sum ([num for num in numero if num % 2 == 0])
    impares=sum ([num for num in numero if num % 2 != 0])
    return total, pares, impares

Cantidadnumeros = int(input("ingrese la cantidad de numeros: "))

numerosindicados= numeroaindicar(Cantidadnumeros)

#sumas
total, pares, impares= sumas(numerosindicados)
print("La suma total es: ", total)
print("La suma de los numeros impares es: ", impares)
print("La suma de los numeros pares es: ", pares)

