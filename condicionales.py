print("### CONDICIONALES -IF- ###")
edad = 19
if edad >= 18:
    print("Eres mayor de edad\n")

edad = 19
if edad >= 18:
    print("Eres  mayor de edad")
else:
    print("Eres menor de edad\n")

edad = 66
if edad >= 18 and edad < 65:
    print("Eres mayor de edad")
elif edad >= 65:
    print("Eres adulto mayor")
else:
    print("Eres menor de edad\n")

edad = 19
print("Usted puede votar"if edad >= 18 else "Usted no puede votar")

print("### BUCLES <CUIDADO CON LOS BUCLES INFINITOS NICOLÁS!!!> ###")
#While <Mientras>
num = 0
while num <= 100:
    print(num)
    num += 2

#PELIGO!! ctrl + c <para cerrar>!#
'''while True:
    print(num)
    num +=2'''

#While (else/if)
while num <= 100:
    print(num)
    num +=2
else:
    print("Mi condición es igual o mayor a 100\n")

while True:
    parametro = input(">")
    if parametro == "exit":
            break
    else:
        print(parametro)

'''RETO 5
    Hacer un algoritmo que detecte si un número es
par o impar, además si es un número primo y si es
mayor o menor a 50. Para este ejercicio se solicita
utilizar condicionales y bucles.'''

'''
licencia = Falce
edad = 19
automovil = False

if licencia:                                            CORRECTO por el "="
    print("puedo porque tengo licencia")
else:
    print("no porque no tengo licencia")
    
    
    

if licencia == True:                                ERRONEO por el "=="
    print("Puedo porque tengo licencia")
else:
    print("No porque no tengo licencia")'''