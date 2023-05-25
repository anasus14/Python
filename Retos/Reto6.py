# Definir tarifas de horas diurnas y nocturnas
tarifa_diurna = 12000
tarifa_nocturna = 16000

# Definir incremento de tarifas los domingos
incremento_diurno_domingo = 2000
incremento_nocturno_domingo = 3000

# Crear diccionario para almacenar la información de los empleados
empleados = {
    "empleado1": ["nocturno", "nocturno", "nocturno", "diurno", "diurno"],
    "empleado2": ["nocturno", "nocturno", "nocturno", "diurno", "diurno", "diurno", "diurno"],
    "empleado3": ["diurno", "diurno", "diurno", "nocturno", "nocturno"]
}

# Calcular el pago diario y total semanal para cada empleado
for empleado in empleados:
    turnos = empleados[empleado]
    pago_diario = 0
    total_semanal = 0
    
    for turno in turnos:
        if turno == "diurno":
            if "domingo" in turnos:
                pago_diario = tarifa_diurna + incremento_diurno_domingo
            else:
                pago_diario = tarifa_diurna
        elif turno == "nocturno":
            if "domingo" in turnos:
                pago_diario = tarifa_nocturna + incremento_nocturno_domingo
            else:
                pago_diario = tarifa_nocturna
        
        total_semanal += pago_diario
    
    empleados[empleado] = {"pago_diario": pago_diario, "total_semanal": total_semanal}

# Imprimir la información de cada empleado
for empleado in empleados:
    info_empleado = empleados[empleado]
    print(f"Empleado: {empleado}")
    print(f"Pago diario: {info_empleado['pago_diario']} CLP")
    print(f"Total semanal: {info_empleado['total_semanal']} CLP")
    print()
