from pathlib import Path


def main():

    ruta = Path("ejercicio7") / "accesos.txt"
    total_accesos = 0
    
    #Lea el fichero completo.
    with open(ruta, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            print(linea)
            total_accesos += 1


    #Cuente el número total de accesos.
    print(f"Total de accesos: {total_accesos}")

    # Obtenga los distintos usuarios que aparecen en el fichero

    usuarios = []
    lineas = []

    with open (ruta,"r",encoding="utf-8") as fichero:
        for linea in fichero:
            lineas.append(linea.split(";"))

    for linea in lineas:
        if linea[0] not in usuarios:
            usuarios.append(linea[0])

    print(usuarios)

    #Cuente cuántos accesos ha realizado cada 
    #Determine qué usuario ha realizado más accesos

    nombre_mas_registros = None
    mas_registros = 0

    for usuario in usuarios:
        contador = 0
        for linea in lineas:
            if usuario == linea[0]:
                contador+=1
        if contador > mas_registros:
            mas_registros = contador
            nombre_mas_registros = usuario
        print(f"{usuario}: {contador} veces")

    print(f"Usuario con mas registros: {nombre_mas_registros}")


    #Genere un fichero llamado resumen.txt

    ruta_resumen = Path("ejercicio7") / "resumen.txt"

    with open(ruta_resumen, "w", encoding="utf-8") as fichero:
        fichero.write("RESUMEN DE ACCESOS \n")
        fichero.write("------------------ \n")
        fichero.write("\n")

        fichero.write(f"Total de accesos: {total_accesos} \n")
        fichero.write(f"Usuarios diferentes: {len(usuarios)} \n")
        fichero.write("\n")

        for usuario in usuarios:
            contador = 0
            for linea in lineas:
                if usuario == linea[0]:
                    contador+=1
            fichero.write(f"{usuario}: {contador} veces \n")

        fichero.write("\n")
        fichero.write(f"Usuario con mas accesos: {nombre_mas_registros}")





if __name__ == "__main__":
    main()