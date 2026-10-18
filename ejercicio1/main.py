movimientos = [
    "entrada", "entrada", "entrada", "salida",
    "entrada", "entrada", "salida", "salida",
    "entrada", "entrada", "entrada", "entrada"
]


def main():

    #1 Procesar todos los movimientos en el orden en el que aparecen.

    vehiculos_aparcados = 0

    for movimiento in movimientos:
        if movimiento == "entrada":
            vehiculos_aparcados+=1
        else:
            vehiculos_aparcados-=1

    # 2. Impedir que el número de vehículos sea menor que 0.

    if vehiculos_aparcados < 0:
        print("Error, no puede haber menos de 0 vehiculos")

    print(f"Vehiculos dentro: {vehiculos_aparcados}")
    

    # 3. Impedir nuevas entradas si el aparcamiento está completo.

    if vehiculos_aparcados == 20:
        print("Aparcamiento completo")

    #4. Número de vehículos.
    print(f"Numero de vehiculos: {vehiculos_aparcados}")

    #4.2 Número de plazas libres.
    plazas_libres = 20 - vehiculos_aparcados
    print(f"Plazas libres: {plazas_libres}")

    # 5. Indicar cuál fue el número máximo de vehículos simultáneos.
    max_vehiculos_simultaneos = 0

    vehiculos_aparcados = 0
    for movimiento in movimientos:
        if movimiento == "entrada":
            vehiculos_aparcados+=1
            if vehiculos_aparcados > max_vehiculos_simultaneos:
                max_vehiculos_simultaneos = vehiculos_aparcados
        else:
            vehiculos_aparcados-=1
        
    print(f"Maximo de vehiculos simultaneos: {max_vehiculos_simultaneos}")

    #6. Contar cuántas entradas y salidas se realizaron correctamente.
    salidas = 0
    for movimiento in movimientos:
        if movimiento == "salida":
            salidas += 1

    print(f"Entradas y salidas correctas: {salidas}")


    #7. Mostrar al final el porcentaje de ocupación del aparcamiento.

    porcentaje_ocupacion = (vehiculos_aparcados / 20)*100
    print(f"Porcentaje ocupacion: {porcentaje_ocupacion:.0f}%")


    ampliacion()



def ampliacion():
    op = input("Introduce un movimiento: ")

    while True:
        if op == "fin":
            break

        elif op == "entrada":
            movimientos.append("entrada")

        elif op == "salida":
            movimientos.append("entrada")


if __name__ == "__main__":
    main()