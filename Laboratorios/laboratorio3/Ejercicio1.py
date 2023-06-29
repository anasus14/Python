diccionario = {"Region 8":"BioBio",
    "Region 10":"Los Lagos",
    "Superficie region 8":23890,
    "Superficie region 10":48583,
    "Habitantes region 8":1556805,
    "habitantes region 10":828708}
print(diccionario)
Superficieregion8= 23890
Superficieregion10=48583
Habitantesregion8=1556805
Habitantesregion10=828708
Densidad1=float(Habitantesregion8 / Superficieregion8)
Densidad2=float(Habitantesregion10/Habitantesregion8)
diccionario["Densidad1"] = f"{Densidad1:.1f}"
diccionario["Densidad2"] = f"{Densidad2:.1f}"
diccionario["capital 8"]="Concepcion"
diccionario["Capital 10"]="Puerto Montt"
Comunas8= ["Lota", "Lebu", "Los Angeles"]
comunas10=["Castro", "Puerto Varas", "Purranque"]
diccionario["Comunas region 8"]=Comunas8
diccionario["Comunas region 10"]=comunas10
Provincia8=("Biobio", "Arauco", "Concepcion")
Provincia10=("Osorno", "Llanquihue", "Chiloe", "Palena")
diccionario["Provincias region 8"]=Provincia8
diccionario["Provincias region 10"]=Provincia10

print(diccionario)




