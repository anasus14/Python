diccionario={
    "Los Rios":14,
    "Araucania":9,
    "Superficie 14": 18429,
    "Superficie 9":31842,
    "Habitantes 14":404432,
    "Habitantes 9":1046322
}
print(diccionario)
superficie14=18429
superficie9=31842
Habitantes14=404432
Habitantes9=1046322

Densidad14=(Habitantes14/superficie14)
Densidad9=(Habitantes9/superficie9)

diccionario["Densidad region 14"]= f"{Densidad14:.3f}"
diccionario["Densidad region 9"]= f"{Densidad9:.3f}"
diccionario["Capital region 14"]="Valdivia"
diccionario["Capital region 9"]="Temuco"

Comunas14=["Rio Bueno", "La Union", "Paillaco"]
Comunas9=["Villarica", "Puren", "Angol"]

diccionario["Comunas region 14"]=Comunas14
diccionario["Comunas region 9"]=Comunas9

Provincias14=("Ranco", "Valdivia")
Provincias9=("Cautin", "Malleco")

diccionario["Provincias region 14"]=Provincias14
diccionario["Provincias region 9"]=Provincias9

Coordenadas=(-53.1625, -70.9225)

diccionario["Coordenadas"]=Coordenadas

print(diccionario)