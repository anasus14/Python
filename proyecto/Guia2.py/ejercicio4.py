def identificacion():
    usuario=input("Ingrese su nombre de usuario: ")
    return usuario

def ingresarcontraseña():
    contraseña=input("Ingrese su contraseña de 4 digitos: ")
    while len(contraseña) !=4:
        print("La contraseña es invalida")
        contraseña=input("Ingrese nuevamente su contraseña de 4 digitos")
    return contraseña

def saldo_total(saldo):
    saldo= input("Su saldo total es: ", saldo)
    return saldo

def girar(saldo):
    giro= int(input("Ingrese el monto a girar: "))
    if giro > saldo:
        print("Su saldo es insuficiente")
    else:
        giro-=saldo
        print("Usted hizo un giro de: ", giro, "pesos")
    return giro

def ingreso(saldo):
    monto=int(input("Ingrese el monto a depositar: "))
    if monto < 0:
        print("El monto ingresado es incorrecto")
    else:
        saldo += monto
    print("Ha recibido", monto, "pesos.")
    return saldo

#Datos a ingresar
saldo_inicial= 20000
usuario= 123456789
contraseñacorrecta= 1234

#Iniciar sesion
sesion=identificacion()
contraseña=ingresarcontraseña()
if sesion == usuario and contraseña == contraseñacorrecta:
    print("Ha iniciado sesion de manera exitosa")
    saldo= saldo_inicial
    #menus
    opcion = 0
    while opcion != 4:
        print("----- MENÚ -----")
        print("1. Consultar saldo")
        print("2. Girar dinero")
        print("3. Recibir dinero")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion== 1:
            saldo_total(saldo)
        elif opcion== 2:
            girar(saldo)
        elif opcion == 3:
            ingreso(saldo)
        elif opcion == 4:
            print("Gracias por utilizar el cajero.")
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")
    else:
        print("Identificación o contraseña incorrecta. Inicio de sesión fallido.")