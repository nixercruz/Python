"""
Se usa el módulo datetime para que al momento de registrar alguna novedad se integre de manera automática la fecha del registro, el 
usuario puede elegir si dejar la fecha que se genera automáticamente o poner una fecha de manera manual.
Se usa para evitar que el usuario registre de manera errónea una fecha que no coincida con el día del registro
"""

import datetime

equipos = {}
novedades = []

# Definir función de agregar un nuevo equipo
def agregar_equipo():
    id_equipo = input("Ingrese el ID del equipo: ")

    # Valida si el id del equipo ya está registrado
    if id_equipo in equipos:
        print("Este equipo ya existe.")
    else:
        cargador = input("¿Tiene cargador? (Sí/No): ")
        mouse = input("¿Tiene mouse? (Sí/No): ")

        # Identificar la clave única y usar un diccionario anidado para la información del equipo
        equipos[id_equipo] = {
            "cargador": cargador,
            "mouse": mouse,
            "estado": "Sin novedades"
        }
        print("Equipo agregado exitosamente.")

# Definir la función de modificar un equipo
def modificar_equipo():
    id_equipo = input("Ingrese el ID del equipo a modificar: ")

    # Validar que el id del equipo se encuentre en el diccionario
    if id_equipo in equipos:
        # Actualizar el estado de los componentes registrados
        equipos[id_equipo]["cargador"] = input("Nuevo estado del cargador: ")
        equipos[id_equipo]["mouse"] = input("Nuevo estado del mouse: ")
        print("Equipo modificado exitosamente.")
    else:
        print("El equipo no se encuentra registrado.")

# Definir la función de eliminar un equipo
def eliminar_equipo():
    id_equipo = input("Ingrese el ID del equipo a eliminar: ")

    # Validar que el id del equipo se encuentre en el diccionario
    if id_equipo in equipos:
        # Eliminar los datos relacionados a la clave única 
        del equipos[id_equipo]
        print("Equipo eliminado correctamente.")
    else:
        print("El equipo no existe.")

# Definir la función de mostrar los equipos registrados 
def mostrar_equipos():
    print("LISTA DE EQUIPOS ")
    # Validar si hay equipos registrados
    if len(equipos) == 0:
        print("No hay equipos registrados.")
    else:
        # Recorrer el diccionario y mostrar los datos guardados 
        for id_eq in equipos:
            print("ID:", id_eq)
            print("Cargador:", equipos[id_eq]["cargador"])
            print("Mouse:", equipos[id_eq]["mouse"])
            print("Estado:", equipos[id_eq]["estado"])
            print("-" * 20)

# Definir la función de buscar equipos 
def buscar_equipo():
    id_equipo = input("Ingrese el ID del equipo a buscar: ")

    # Validar si el id del equipo está en el diccionario
    if id_equipo in equipos:
        # Mostrar la información del equipo guardada en el diccionario y el diccionario anidado
        print("INFORMACIÓN DEL EQUIPO ")
        print("ID:", id_equipo)
        print("Cargador:", equipos[id_equipo]["cargador"])
        print("Mouse:", equipos[id_equipo]["mouse"])
        print("Estado:", equipos[id_equipo]["estado"])
    else:
        print("No se encuentra el equipo.")

# Definir la función de registrar alguna novedad
def agregar_novedad():
    id_equipo = input("Ingrese el ID del equipo con novedad: ")

    # Validar si el id del equipo está en el diccionario 
    if id_equipo in equipos:
        # Usar el módulo adicional datetime para poner la fecha  actual automáticamente
        fecha_automatica = datetime.datetime.now().strftime("%d/%m/%Y")
        print("Fecha automática del sistema:" ,fecha_automatica)

        # Verificar si el usuario desea usar la fecha automática o quiere poner una fecha de manera manual
        usar_actual = input("¿Desea usar esta fecha? (Sí/No): ").lower()
        if usar_actual == "si" or usar_actual == "s":
            fecha = fecha_automatica
        else:
            fecha = input("Ingrese la fecha manualmente (DD/MM/AA): ")
            
        descripcion = input("Describa la novedad: ")

        # Registrar la novedad en un diccionario 
        novedad = {
            "id": id_equipo,
            "fecha": fecha,
            "descripcion": descripcion
        }
        # Agregar la novedad a la lista con su respectiva información 
        novedades.append(novedad)
        
        equipos[id_equipo]["estado"] = "Con novedades"
        print("Novedad registrada correctamente.")
    else:
        print("El equipo no existe, regístrese primero.")

# Definir la función de los registros de las novedades 
def reporte_novedades():
    print("REPORTE DE NOVEDADES ")
    # Validar que hayan novedades registradas
    if len(novedades) == 0:
        print("No hay novedades registradas.")
    else:
        # Mostrar la información de las novedades registradas 
        for nov in novedades:
            print("Equipo ID:", nov["id"])
            print("Fecha:", nov["fecha"])
            print("Descripción:", nov["descripcion"])
            print("-" * 20)

# Menu principal
while True:
    print("CONTROL DE EQUIPOS Y NOVEDADES ")
    print("1. Agregar equipo")
    print("2. Modificar equipo")
    print("3. Eliminar equipo")
    print("4. Mostrar lista de equipos")
    print("5. Buscar equipo por ID")
    print("6. Agregar novedad")
    print("7. Ver reporte de novedades")
    print("8. Salir")
    
    opcion = int(input("Seleccione una opción (1-8): "))
    
    match opcion:
        case 1:
            agregar_equipo()
        case 2:
            modificar_equipo()
        case 3:
            eliminar_equipo()
        case 4:
            mostrar_equipos()
        case 5:
            buscar_equipo()
        case 6:
            agregar_novedad()
        case 7:
            reporte_novedades()
        case 8: 
            print("Fin del programa")
            break
        case _:
            print ("Opción inválida")
            salir = input()