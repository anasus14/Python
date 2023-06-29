#Ejercicio número 3:
def añobisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

año = 0
while año <= 100:
    if añobisiesto(año) and añobisiesto(0):
        print(año,"Es un año bisiesto")
    else:
        print(año,"No es un año bisiesto")
    año += 1
