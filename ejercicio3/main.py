puntuaciones = {
    "Mario": 1250,
    "Lucía": 890,
    "Carlos": 1420,
    "Ana": 1100
}

def añadir_jugador(nombre,puntuacion):
    if nombre in puntuaciones:
        print("El jugador ya existe")
    else:
        puntuaciones[nombre] = puntuacion


def modificar_puntuacion(nombre):
    if nombre in puntuaciones:
        nueva_puntuacion = int(input("Nueva puntuacion: "))
        puntuaciones[nombre] = nueva_puntuacion
    else:
        print("Ese jugador no existe")


def eliminar_jugador(nombre):
    if nombre in puntuaciones:
        puntuaciones.pop(nombre)
    else:
        print("Jugador no existe")


def consular_jugador(nombre):
    if nombre in puntuaciones:
        print(f"Nombre: {nombre}, puntuacion: {puntuaciones[nombre]}")


def mostrar_mejor_jugador():

    mayor_puntuacion = max(puntuaciones.values())
    nombre = ""
    for jugador in puntuaciones:
        if puntuaciones[jugador] == mayor_puntuacion:
            nombre = jugador

    print(f"Jugador: {nombre}, {mayor_puntuacion}")

    
def mostrar_jugadores_mayor(puntos):

    for jugador in puntuaciones:
        if puntuaciones[jugador] > puntos:
            print(jugador)


def puntuacion_media():
    media = sum(puntuaciones.values())/len(puntuaciones)
    print(f"Puntacion media: {media}")


def main():

    while True:
        menu()
        op = int(input("Introduce una opcion: "))

        if op == 8:
            break
        elif op == 1:
            nombre = input("Nombre: ")
            puntuacion = int(input("Puntuacion: "))

            añadir_jugador(nombre,puntuacion)

        elif op == 2:
            nombre = input("Nombre: ")
            modificar_puntuacion(nombre)

        elif op == 3:
            nombre = input("Nombre: ")
            eliminar_jugador(nombre)

        elif op == 4:
            nombre = input("Nombre: ")
            consular_jugador(nombre)

        elif op == 5:
            mostrar_mejor_jugador()

        elif op == 6:
            puntos = int(input("Puntos: "))
            mostrar_jugadores_mayor(puntos)

        elif op == 7:
            puntuacion_media()



def menu():
    print("1. Añadir jugador")
    print("2. Modificar puntuación")
    print("3. Eliminar jugador")
    print("4. Consultar jugador")
    print("5. Mostrar mejor jugador")
    print("6. Mostrar jugadores que superan una puntuación")
    print("7. Mostrar puntuación media")
    print("8. Salir")



if __name__ == "__main__":
    main()