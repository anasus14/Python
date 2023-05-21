edad = 22
estatura = 1.60
peso = 73
complejo = 1+4
print(f"Mi estatura es {estatura} y mi peso es de {peso}")
print ("transformar un valor real a entero", int (peso))
print ("transformar un numero entero a real:", float (edad))
imc=peso/(estatura**2)
print (type(imc))
print ("Mi IMC es de: ", imc, "\n")

print ("Mi IMC es:{:.2F}". format (imc), "\n")

#se puede imprimir con " " """" y 
asignatura = 'programacion'
carrera = "Ingenieria Civil Informatica"
print ("la asignatura de", asignatura, "corresponde a la carrera de", carrera)
print ("la cantidad de caracteres de la palabra", asignatura, "es de:", len(asignatura))
#Len cuenta los caracteres

ampolleta = False #siempre sera 0 de apagado
interruptor = True #siempre sera 1 de encendido
print ("la variable ampolleta es de tipo:", type(interruptor), "\n") #type indica el tipo de datos con el cual estamos trabajando
print(bool(0))
print(bool(" "))
print(bool(None))
print(bool("true"))
print(bool(1))
#buleano es un tipo de dato
#Listas
Estudiantes = ["Alonso", "Alfredo", "Cristobal", "Alonso"]
Otra_lista = list ()
print ("esta es una lista vacia", Otra_lista )
num = [1,2,3,4,5]
Lenguaje = ["Python"]
data = ["Osorno", {'UV : nivel bajo', 'Temp ° C : 15'}, (-40.5725, -73.1353)]
#corchetes para iniciar una lista automaticamente


print("lista de cadena de caracteres:",Estudiantes)
print("lista de numeros:", num)
print("lista de un elemento",Lenguaje)
print("esto igual es una lista", data)
listamixta = ['Felipe', 100, True]
print("Esta igual es una lista", listamixta)
print(len(Lenguaje)) #en una lista len cuenta la cantidad de elementos, siempre va dentro de los parentesis
print(len(num))
print(Estudiantes.count("Alonso"))#count es la cantidad de veces que se repite el elemento en la lista
print(num.count(7))

Lenguaje = ["Java Script"]
print("nuevo valor del arreglo de un elemento", Lenguaje)
print(Estudiantes[1]) #se imprime el elemento 1 de la lista
print(Estudiantes[0]) #0 es el primer elemento de la lista, indice, posicion o index
print("posicion -2", Estudiantes[-2])#cuenta de derecha a izquierda
