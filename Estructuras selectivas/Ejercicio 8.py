'''
 Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el médico se basa para obtener el resultado es la siguiente: EDAD NIVEL HEMOGLOBINA 0 - 1 mes                     13 - 26 g% > 1 y < = 6 meses       10 - 18 g% > 6 y < = 12 meses     11 - 15 g% > 1 y < = 5 años       11.5 - 15 g% > 5 y < = 10 años     12.6 - 15.5 g% > 10 y < = 15 años    13 - 15.5 g% mujeres > 15 años    12 - 16 g% hombres > 15 años   14 - 18 g% 
'''

def evaluar_anemia_interactivo():
    
    print("Seleccione la unidad de edad:")
    print("1. Meses")
    print("2. Años")
    opcion_unidad = input("Ingrese el número de la opción (1 o 2): ").strip()
    
    if opcion_unidad == '1':
        unidad_edad = 'meses'
    elif opcion_unidad == '2':
        unidad_edad = 'anos'
    else:
        print("Opción no válida.")
        return
    
    try:
        edad_valor = float(input(f"Ingrese la edad en {unidad_edad}: "))
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")
        return

    sexo = ""
    if unidad_edad == 'anos' and edad_valor > 15:
        sexo = input("Ingrese el sexo (hombre / mujer): ").strip().lower()

    try:
        hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la hemoglobina.")
        return

    limite_inferior = None

    if unidad_edad == 'meses':
        if 0 <= edad_valor <= 1:
            limite_inferior = 13
        elif edad_valor > 1 and edad_valor <= 6:
            limite_inferior = 10
        elif edad_valor > 6 and edad_valor <= 12:
            limite_inferior = 11
    elif unidad_edad == 'anos':
        if edad_valor > 1 and edad_valor <= 5:
            limite_inferior = 11.5
        elif edad_valor > 5 and edad_valor <= 10:
            limite_inferior = 12.6
        elif edad_valor > 10 and edad_valor <= 15:
            limite_inferior = 13
        elif edad_valor > 15:
            if sexo in ['mujer', 'mujeres', 'femenino']:
                limite_inferior = 12
            elif sexo in ['hombre', 'hombres', 'masculino']:
                limite_inferior = 14
            else:
                print("Sexo no reconocido para el rango de edad.")
                return

    if limite_inferior is None:
        print("La edad ingresada no coincide con ningún rango válido de la tabla.")
        return

    print(f"Límite inferior correspondiente: {limite_inferior} g%")
    if hemoglobina < limite_inferior:
        print("Resultado: POSITIVO (Tiene anemia)")
    else:
        print("Resultado: NEGATIVO (No tiene anemia)")

evaluar_anemia_interactivo()