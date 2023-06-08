def ingresar_identificacion():
    identificacion = input("Ingrese su identificación: ")
    return identificacion

def ingresar_contrasena():
    contrasena = input("Ingrese su contraseña de 4 dígitos: ")
    while len(contrasena) != 4:
        print("La contraseña debe tener exactamente 4 dígitos.")
        contrasena = input("Ingrese su contraseña de 4 dígitos: ")
    return contrasena

def consultar_saldo(saldo):
    print("Su saldo actual es:", saldo)

def girar_dinero(saldo):
    monto = int(input("Ingrese el monto a girar: "))
    if monto > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= monto
        print("Ha girado", monto, "pesos.")
    return saldo

def recibir_dinero(saldo):
    monto = int(input("Ingrese el monto a recibir: "))
    saldo += monto
    print("Ha recibido", monto, "pesos.")
    return saldo

# Datos de prueba
saldo_inicial = 50000
identificacion_correcta = "1234567890"
contrasena_correcta = "1234"

# Inicio de sesión
identificacion = ingresar_identificacion()
contrasena = ingresar_contrasena()

# Verificación de identificación y contraseña
if identificacion == identificacion_correcta and contrasena == contrasena_correcta:
    print("Inicio de sesión exitoso.")
    saldo = saldo_inicial

    # Menú de opciones
    opcion = 0
    while opcion != 4:
        print("----- MENÚ -----")
        print("1. Consultar saldo")
        print("2. Girar dinero")
        print("3. Recibir dinero")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            consultar_saldo(saldo)
        elif opcion == 2:
            saldo = girar_dinero(saldo)
        elif opcion == 3:
            saldo = recibir_dinero(saldo)
        elif opcion == 4:
            print("Gracias por utilizar el cajero.")
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")
    else:
     print("Identificación o contraseña incorrecta. Inicio de sesión fallido.")
