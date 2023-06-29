ciudades = ["Punta arenas", "Temuco", "Santiago", "Osorno"]
ICA = [134, 99, 245, 50]
ICA.sort()
print(ciudades,ICA)

if ICA[0] > 0 and ICA[0] <= 50:
        print(f"{ciudades[0]} tiene un ICA Buena")
if ICA[1] >= 51 and ICA[1] <= 100:
            print(f"{ciudades[1]},tiene un ICA Moderada")
if ICA[2] >= 101 and ICA[2] <= 150:
            print(f"{ciudades[2]},tiene un ICA Dañina a la salud para grupos sencibles")
else:
    if ICA[3] >= 151 and ICA[3] <= 200:
       print(f"{ciudades[3]},tiene un ICA Dañina a la salud")
if ICA[3] >= 201 and ICA[3] <= 300:
         print(f"{ciudades[3]},tiene un ICA Muy dañina a la salud")
else:
        if ICA[3] >= 300:
           print(f"{ciudades[4]},tiene un ICA Peligrosa")