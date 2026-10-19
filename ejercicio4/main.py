diccionario = {
    "casa": "house",
    "coche": "car",
    "libro": "book",
    "mesa": "table"
}

def traduccir_palabra(palabra):
    if palabra in diccionario:
        print(diccionario[palabra])
    else:
        print("La palabra no esta en el diccionario")


def añadir_traduccion(palabra_español,palabra_ingles):
    if palabra_español not in diccionario:
        diccionario[palabra_español] = palabra_ingles
    else:
        print("La traduccion ya existe")


def modificar_traduccion(palabra_español):
    if palabra_español in diccionario:
        nueva_traduccion = input(f"Nueva traduccion para {palabra_español}")
        diccionario[palabra_español] = nueva_traduccion
    else:
        print("La palabra no esta en el diccionario")


def eliminar_palabra(palabra_español):
    if palabra_español in diccionario:
        diccionario.pop(palabra_español)
    else:
        print("La palabra no esta en el diccionario")   

def ordenar_palabras():
    diccionario_ordenado = sorted(diccionario)
    print(diccionario_ordenado)

def traduccir_frase(frase):
    palabras = frase.split(" ")
    frase_traducida = ""

    for palabra in palabras:
        if palabra in diccionario:
            frase_traducida += diccionario[palabra] + " "
        else:
            frase_traducida+= palabra + " "

    print(frase_traducida)


def main():

    while True:
        menu()
        op = int(input("Introduce una opcion: "))

        if op == 7:
            break
        elif op == 1:
            palabra = input("Palabra: ")
            traduccir_palabra(palabra)

        elif op == 2:
            palabra_español = input("Palabra en español: ")
            palabra_ingles = input("Palabra en ingles: ")

            añadir_traduccion(palabra_español,palabra_ingles)

        elif op == 3:
            palabra_español = input("Palabra en español: ")

            modificar_traduccion(palabra_español)

        elif op == 4:
            palabra_español = input("Palabra en español: ")
            eliminar_palabra(palabra_español)

        elif op == 5:
            ordenar_palabras()

        elif op == 6:
            frase = input("Introduce una frase: ")
            traduccir_frase(frase)


def menu():
    print("1. Traducir una palabra")
    print("2. Añadir una nueva traduccion")
    print("3. Modificar una traducción existente")
    print("4. Eliminar una palabra")
    print("5. Mostrar todas las palabras ordenadas alfabéticamente")
    print("6. Traducir una frase")
    print("7. Salir")




if __name__ == "__main__":
    main()