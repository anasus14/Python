nombre=input("ingrese el nombre del estudiante: ")
asignatura=input("ingrese la asignatura correspondiente: ")
Notalab1=float(input("ingrese nota laboratorio 1: "))
Notalab2=float(input("ingrese nota del laboratorio 2: "))
Notafinal=(Notalab1)*0.3+int(Notalab2)*0.7

Diccionario={
    "nombre":nombre,
    "asignatura": asignatura,
    "Nota final":f"Notafinal:.1.f"}
print("Diccionario final", Diccionario)
