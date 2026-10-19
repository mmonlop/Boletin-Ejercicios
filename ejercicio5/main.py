peliculas = [
    {
        "titulo": "Matrix",
        "anio": 1999,
        "genero": "Ciencia ficción",
        "puntuacion": 8.7
    },
    {
        "titulo": "Gladiator",
        "anio": 2000,
        "genero": "Drama",
        "puntuacion": 8.5
    }
]

def menu():

    print("1. Añadir una película")
    print("2. Buscar una película por título")
    print("3. Mostrar todas las películas")
    print("4. Mostrar las películas de un género determinado")
    print("5. Mostrar películas posteriores a un año indicado")
    print("6. Calcular la puntuación media de todas las películas")
    print("7. Mostrar la película mejor valorada")
    print("8. Eliminar una película")
    print("9. Salir")


    
def añadir_pelicula(pelicula):
    existe = False
    for peli in peliculas:
        if peli['titulo'] == pelicula['titulo']:
            print("ya existe")
            existe = True
       

    if not existe:
        peliculas.append(pelicula)
        print("Pelicula añadida")
       
    
def buscar_pelicula(titulo):
    for pelicula in peliculas:
        if pelicula['titulo'] == titulo:
            print(pelicula)
            return

    print("Pelicula no encontrada")
        

def mostrar_peliculas():
    for pelicula in peliculas:
        print(f"TITULO: {pelicula['titulo']}, AÑO: {pelicula['anio']}, GENERO: {pelicula['genero']}, PUNTUACION: {pelicula['puntuacion']}")


def mostrar_peliculas_genero(genero):

    for pelicula in peliculas:
        if pelicula['genero'] == genero:
            print(pelicula['titulo'])
            return

    print("No hay peliculas con ese genero")


def mostrar_peliculas_anio(anio):
    for pelicula in peliculas:
        if pelicula['anio'] > anio:
            print(pelicula['titulo'])

    

def calcular_puntuacion_media():
    total =0

    for pelicula in peliculas:
        total += pelicula['puntuacion']

    print(f"PUNTUACION MEDIA: {total / len(peliculas)}")


def pelicula_mejor_valorada():
    mejor_valoracion = 0
    nom_peli = ""

    for pelicula in peliculas:
        if pelicula['puntuacion'] > mejor_valoracion:
            mejor_valoracion = pelicula['puntuacion']
            nom_peli = pelicula['titulo']

    print(f"PELICULA MEJOR VALORADA: {nom_peli}, VALORACION: {mejor_valoracion}")


def eliminar_pelicula(titulo):

    for pelicula in peliculas:
        if pelicula['titulo'] == titulo:
            peliculas.remove(pelicula)
            print("Pelicula eliminada")
            return

    print("La pelicula no existe")


def main():

    while True:
        menu()
        op = int(input("Introduce una opcion: "))

        if op == 1:

            titulo = input("Titulo: ")
            anio = input("Año: ")
            genero = input("Genero: ")
            puntuacion = input("Puntuacion: ")

            pelicula = {"titulo":titulo, "anio": anio, "genero": genero, "puntuacion":puntuacion}

            añadir_pelicula(pelicula)

        elif op == 2:
            titulo = input("Titulo: ")

            buscar_pelicula(titulo)

        elif op == 3:
            mostrar_peliculas()

        elif op == 4:
            genero = input("Genero a buscar: ")
            mostrar_peliculas_genero(genero)

        elif op == 5:
            anio = int(input("Año a buscar: "))
            mostrar_peliculas_anio(anio)

        elif op == 6:
            calcular_puntuacion_media()

        elif op == 7:
            pelicula_mejor_valorada()

        elif op == 8:

            titulo = input("Titulo de la pelicula: ")
            eliminar_pelicula(titulo)


        elif op == 9:
            break




if __name__ == "__main__":
    main()