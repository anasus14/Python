#Ejercicio número 2:
def ingresarnombres():
    nombres = 0
    while nombres < 3:
        nombres = nombres + 1
        ingresarnombres = input("Ingrese los nombres: ")
        nomb.append(ingresarnombres)
        print(nomb)
nomb = []
ingresarnombres()

def contarlista(listnombr):
    letras = 0
    for nombre in listnombr:
        if isinstance(nombre, str):
            letras += len(nombre)
    return letras
totalletras = contarlista(nomb)
print(totalletras)

def impresionresultados():
    print(f"Los nombres ingresados son: {nomb} y la cantidad de letras que la componen en total es de: {totalletras}")
impresionresultados()
