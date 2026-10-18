# Ejercicio 2. Análisis de ventas semanales #
dias = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
]

ventas = [1250, 980, 1430, 2100, 1750, 900, 2350]

def main ():

    #1. venta total de la semana
    venta_total_semana = sum(ventas)

    print(f"Venta total de la semana: {venta_total_semana}")

    #2. media diaria de ventas
    media_diaria_ventas = venta_total_semana/ len(dias)

    print(f"Media diaria de ventas: {media_diaria_ventas:.2f}")

    #3. días cuyas ventas superaron la media

    dias_superior_media = []

    for i,venta in enumerate(ventas):
        if venta > media_diaria_ventas:
            dias_superior_media.append(dias[i])

    print(dias_superior_media)


    #4.1. Día con mayor número de ventas

    dia_mas_ventas = ""
    mayor_venta=0
    pos = 0

    for i,venta in enumerate(ventas):
        if venta > mayor_venta:
            mayor_venta = venta
            pos = i

    dia_mas_ventas = dias[pos]

    print(f"Dia con mayor numero de ventas: {dia_mas_ventas}, total: {mayor_venta}")
    
    #4.2. Día con menor número de ventas
    
    dia_menos_ventas = ""
    menor_venta = max(ventas)
    pos = 0

    for i,venta in enumerate(ventas):
        if venta < menor_venta:
            menor_venta = venta
            pos = i

    dia_menos_ventas = dias[pos]

    print(f"Dia con menor numero de ventas: {dia_menos_ventas}, total: {menor_venta}")


    #5. Cuente cuántos días se superaron los 1.500 €

    dias_superior_mil = [venta for venta in ventas if venta > 1500]

    print(f"Dias que superaron los 1500€: {len(dias_superior_mil)}")

    #6. porcentaje de las ventas semanales corresponde al mejor día

    pct_mejor_dia = (mayor_venta / venta_total_semana) *100

    print(f"Porcentaje del dia {dia_mas_ventas}: {pct_mejor_dia:.2f}%")

    #7. días ordenados de mayor a menor venta




if __name__ == "__main__":
    main()