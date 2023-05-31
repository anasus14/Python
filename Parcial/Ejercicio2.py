'''Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1.0 ni
mayores a 7.0.'''
notas=float(input("ingresa tus notas"))
if notas <1.0 :
    print("ingrese un numero correcto")
    if notas > 7.0:
        print("ingrese un numero correcto")
notas2=float(input("ingresa tus notas"))
if notas2 <1.0 :
    print("ingrese un numero correcto")
    if notas2 > 7.0:
        print("ingrese un numero correcto")
notas3=float(input("ingresa tus notas"))
if notas3 <1.0 :
    print("ingrese un numero correcto")
    if notas3 > 7.0:
        print("ingrese un numero correcto")
notas4=float(input("ingresa tus notas"))
if notas4 <1.0 :
    print("ingrese un numero correcto")
    if notas4 > 7.0:
        print("ingrese un numero correcto")
notas5=float(input("ingresa tus notas"))
if notas5 <1.0 :
    print("ingrese un numero correcto")
    if notas5 > 7.0:
        print("ingrese un numero correcto")
notas6=float(input("ingresa tus notas"))
if notas6 <1.0 :
    print("ingrese un numero correcto")
    if notas6 > 7.0:
        print("ingrese un numero correcto")
notas7=float(input("ingresa tus notas"))
if notas7 <1.0 :
    print("ingrese un numero correcto")
    if notas7 > 7.0:
        print("ingrese un numero correcto")
notas8=float(input("ingresa tus notas"))
if notas8 <1.0 :
    print("ingrese un numero correcto")
    if notas8 > 7.0:
        print("ingrese un numero correcto")
notas9=float(input("ingresa tus notas"))
if notas9 <1.0 :
    print("ingrese un numero correcto")
    if notas9 > 7.0:
        print("ingrese un numero correcto")
notas10=float(input("ingresa tus notas"))
if notas10 <1.0 :
    print("ingrese un numero correcto")
    if notas10 > 7.0:
        print("ingrese un numero correcto")

notasfinales=[notas, notas2, notas3, notas4, notas5, notas6, notas7, notas8, notas9, notas10]

#Calcular la media
media=sum(notasfinales)/10

print(media)