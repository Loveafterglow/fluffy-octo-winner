def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar hábito")
    print("2. Buscar hábito")
    print("3. Eliminar hábito")
    print("4. Actualizar estado")
    print("5. Mostrar hábitos")
    print("6. Salir")
    print("===================================")

def leer_opcion():
    opcion = 0

    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Error: la opción debe estar entre 1 y 6. ")
        except ValueError:
            print("Error: debe ingresar un número entero. ")
    return opcion


mostrar_menu()
opcion = leer_opcion()