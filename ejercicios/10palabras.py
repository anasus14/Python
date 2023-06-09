
#Palabra=input("Ingrese su palabra: ")
#for i in range(10):
  #  print(Palabra)

#Escribir un programa que pregunte al usuario su edad y muestre 
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
#edad=int(input("Ingrese su edad"))
#for i in range (1,edad):
    #print(i)

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los 
#números impares desde 1 hasta ese número separados por comas.
#numero=[]
#numero=int(input("Ingrese su numero: "))
#for i in range (1, numero+1, 2):
    #print(i, end=",")

#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''numero=[]
numero=int(input("Ingrese un numero positivo: "))
if numero < 0:
    print("El numero ingresado es incorrecto: ")
    numero=input(input("ingrese un numero positivo"))
for i in range(numero,-1, -1):
    print(i, end=",")'''

v=[]
num= int(input("numero positivo"))
if num<0 : 
    print("el numero es negativo")
else: 
    for i in range (num +1 ): 
        v.append(i)
        print(v)
        v.sort()
        print(v)