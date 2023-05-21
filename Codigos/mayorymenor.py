n1=int(input("ingresa un numero"))
n2=int(input("ingresa un numero"))
n3=int(input("ingresa un numero"))
if n1!=n2 and n1!=n3 and n2!=n3:
    if n1 > n2:
            if n1 > n3:
                         print("El numero mayor es: ", n1)
            else:
                print("El numero mayor es: ", n3)
    else:
           if n2 > n3:
                  print("El numero mayor es: ", n2)
           else:
                  print("El numero mayor es: ", n3)
    if n1 < n2:
           if n1 < n3:
                  print("El numero menor es: ", n1)
           else:
                  print("El numero menor es:", n3)
    else:
           if n2<n3:
                  print("El numero menor es: ", n2)
           else:
                  print("El numero menor es: ", n3)
else:
    print("ingresa 3 numeros diferentes")
