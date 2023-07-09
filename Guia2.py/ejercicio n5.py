#Ejercicio número 5
def obtenernumeros():
    numeros = []
    while True:
        numero = int(input("Ingrese un número entero positivo (-1 para terminar): "))
        if numero == -1:
            break
        if numero < 0:
            print("Número inválido. Ingrese un número entero positivo.")
            continue
        numeros.append(numero)
    return numeros

def calcularmayor(numeros):
    mayor = max(numeros)
    return mayor

def calcularsumatoria(numeros):
    sumatoria = sum(numeros)
    return sumatoria

def pares(numeros):
    sumatoria_pares = sum([num for num in numeros if num % 2 == 0])
    return sumatoria_pares

def impares(numeros):
    sumatoria_impares = sum([num for num in numeros if num % 2 != 0])
    return sumatoria_impares

def promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    return promedio

# Obtener los números
numeros_ingresados = obtenernumeros()

# Calcular resultados
mayor = calcularmayor(numeros_ingresados)
sumatoria_total = calcularsumatoria(numeros_ingresados)
sumatoria_pares = pares(numeros_ingresados)
sumatoria_impares = impares(numeros_ingresados)
promedio = promedio(numeros_ingresados)

# Imprimir resultados
print("Número mayor:", mayor)
print("Sumatoria total:", sumatoria_total)
print("Sumatoria de números pares:", sumatoria_pares)
print("Sumatoria de números impares:", sumatoria_impares)
print("Promedio:", promedio)

# Comparar el número mayor con el promedio
if mayor > promedio:
    print("El número mayor es mayor que el promedio.")
elif mayor < promedio:
    print("El número mayor es menor que el promedio.")
else:
    print("El número mayor es igual al promedio.")