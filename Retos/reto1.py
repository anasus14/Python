#Escribe un programa que le pregunte al usuario su nombre y edad, y luego calcule e imprima cuantos años tendra en 20 años.
#el programa debe imprimir "Hola mi nombre [nombre], tengo [edad] años y en 20 años tendre [total] años"
nombre=input("¿Cual es tu nombre?\n")
edad= input("¿Cual es tu edad?\n")
total= 20 + int(edad)
print (f"Hola mi nombre es ", nombre, "tengo ", edad, "años y en 20 años tendre ", total, "años.")