def obtener_longitudes(frase):
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

frase_usuario = input("Ingresa una frase: ")
resultado = obtener_longitudes(frase_usuario)
print(resultado)

