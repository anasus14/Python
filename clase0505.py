#las listas son mutables, pueden tener scrpt, textos numeros, listas dentro de otras listas
#es mutable al poder modificarla.
#las tuplas son una colleccion ordenadas de datos, se pueden acceder a posiciones donde el 0 es la primera 
#posicion, son datos indexados a diferencia de las listas las tuplas no se pueden modificar.
#se pueden tener textos, numeros, tuplas dentro de otra y listas, si se tiene una lista dentro de una tupla la lista
#la lista si se puede modificar haciendo una copia de la lista porque la tupla no se puede editar.
#puede tener muchos y diferentes tipos de elementos.
#es mas eficiente.
#type indica que es
#List[]  Tupla()   SET {}  diccionario {}

newtupla = tuple() 
grupo1=("Daniel", "Andres")
print(type(grupo1))
print("indice del elemento:", grupo1.index("Daniel"))

#los SET {} o conjuntos son no ordenados por lo que no se puede consultar la posicion.
#se utilizan para unir elementos, solo pueden contener objetos de elemento inmutables
nuevoconjunto=set({"Amarillo", "Azul", "Naranja"})
 #se imprime un diccionario al no tener datos
Animales=set()
Animales.add("Celeste")
print
diccionario1=dict()
#se llaman mapas en otros lenguajes
datos_personales={
    "Nombre":"Susana",
    "institucion":"Ulagos",
    "Edad":22,
    "Asignatura":"Estructura de datos"}
print("diccionario inicial", datos_personales)
print(len(datos_personales))
print(datos_personales["institucion"])
datos_personales["institucion"]="USS"
datos_personales["Ciudad"]="Osorno"
print("Datos actualizado:", datos_personales)
del datos_personales["Ciudad"]
print("Datos actualizados:", datos_personales)

