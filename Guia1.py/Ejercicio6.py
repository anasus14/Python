print("Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos de un dia desde las 00:00:00 horas hasta las 23:59:59 horas.")

for hora in range (0,23):
    for minutos in range (0,59):
        for segundos in range (0,59):
            print("La Hora es: ", f"{hora:02d}:{minutos:02d}:{segundos:02d}")
