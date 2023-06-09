#Un algoritmo con una lista que contenga los numeros del 1 al 10 ordenarla de manera ascendente, descendente,
#eliminar el 8, agregar el 11.
#Sumar todos los elementos, sumar pares, sumar impares.
numeros=[1,2,3,4,5,6,7,8,9,10]
print(sorted(numeros))
descendente= numeros.sort()
print(descendente)
numeros.pop(7)
print("Aqui la lista sin el 8", numeros)
numeros.append(11)
print("Aqui la lista con el 11", numeros)

total=sum(numeros)
pares= sum ([num for num in numeros if num % 2 == 0])
impares=sum ([num for num in numeros if num % 2 != 0])
    
print("La suma total es: ", total )
print("La suma de los numeros impares es: ", pares)
print("La suma de los numeros pares es: ", impares)
