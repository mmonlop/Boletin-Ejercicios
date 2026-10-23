import csv
from pathlib import Path
import json

def main():

    ruta = Path("ejercicio8") / "productos.csv"
    productos = []
    ruta_json = Path("ejercicio8") / "productos.json"


    #Lea los productos del fichero CSV + almacenar 
    with open(ruta,"r",encoding="utf-8") as fichero:
        lector = csv.DictReader(fichero)

        for linea in lector:
            if linea not in productos:
                productos.append(linea)

    #mostrar
    print(productos)

    #Muestre los productos cuyo stock sea inferior a 5 unidades
    print("PRODUCTOS CON STOCK MENOR A 5: ")
    for producto in productos:
        if int(producto["stock"]) < 5:
            print(producto)

    #Calcule el valor total del inventario
    total_inventario = 0

    for producto in productos:
        total_inventario += float(producto["precio"]) * int(producto["stock"])

    print(f"TOTAL INVENTARIO: {total_inventario}")



    while True:
        menu()
        op = int(input("Introduce una opcion: "))


        if op == 1:
            codigo = input("Introduce el codigo: ")

            for producto in productos:
                if producto["codigo"] == codigo:
                    print(producto)

        elif op == 2:
            codigo = input("Introduce el codigo: ")

            for producto in productos:
                if producto["codigo"] == codigo:
                    nuevo_stock = int(input("Nuevo stock: "))
                    producto["stock"] = nuevo_stock
        
        elif op == 3:

            with open(ruta_json, "w", encoding="utf-8") as fichero:
                json.dump(productos, fichero, ensure_ascii=False)

        elif op == 0:
            break


def menu():
    print("1.Buscar producto por codigo: ")
    print("2.Modificar stock de un producto: ")
    print("3.Guardar los datos actualizados: ")
    print("0.Salir: ")





if __name__ == "__main__":
    main()