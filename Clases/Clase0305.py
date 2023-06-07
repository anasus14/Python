Lista_1= [1, 2, 3, 4]
Lista_2= list("Matias", "Andres")

print("suma de listas", Lista_1+Lista_2)
print(list(Lista_1))
print(list(range(1,4)))
#Tuplasd no mutables
newtupla= tuple()
Grupo1= ("daniel", "Cristian", "Felipe", "200", "daniel")
print("#####Tuplas####")
print(Grupo1[0])
#Consultando el elemento daniel
print("El elemento se repite:", Grupo1.count("daniel"))
print("indice del elemento", Grupo1.index("daniel"))
#reasignando el primer elemento de la tuple
Grupo1[1]= "Andrea"
print(Grupo1)
#obteniendo un trozo de la tupla
Grupo_2= ("Pedro", 100, "Felipe", "Diego", 2020, "Alejandra")
print("Trozo de la tupla", Grupo_2[0:3])

#Como puedo modificar una tupla?
Grupo1 = list(Grupo1)
#SETS conjuntos
Conjunto_vacio= set()
Conjunto_vacio1={} #diccionario o set?
print(type(Conjunto_vacio1))
conjunto_valores= set({"azul", "Rojo", "Verde"}) #utilizando la funcion set
conjunto_animales= set ("gatos", "perro", "loro") #Utilizando llaves
print("el primer set contiene los siguientes colores:", conjunto_valores)
print("el set contiene los siguientes elementos", conjunto_animales)
print(conjunto_animales[0]) #accediendo al primer elemento, pero no se puede consultar posicion al igual que en tupla.
conjunto_valores.add("Celeste")
print("El set de colores lo conforman", conjunto_valores)
#set no permite elementos duplicados