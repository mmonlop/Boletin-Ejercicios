
pedidos = [
    {
        "numero": 101,
        "cliente": "Ana",
        "importe": 125.50,
        "estado": "pendiente"
    },
    {
        "numero": 102,
        "cliente": "Luis",
        "importe": 89.90,
        "estado": "enviado"
    },
    {
        "numero": 103,
        "cliente": "Carlos",
        "importe": 210.75,
        "estado": "entregado"
    },
    {
        "numero": 104,
        "cliente": "María",
        "importe": 45.99,
        "estado": "pendiente"
    },
    {
        "numero": 105,
        "cliente": "Javier",
        "importe": 320.00,
        "estado": "enviado"
    },
    {
        "numero": 106,
        "cliente": "Lucía",
        "importe": 67.50,
        "estado": "cancelado"
    },
    {
        "numero": 107,
        "cliente": "Pedro",
        "importe": 154.25,
        "estado": "entregado"
    },
    {
        "numero": 108,
        "cliente": "Sofía",
        "importe": 98.80,
        "estado": "pendiente"
    },
    {
        "numero": 109,
        "cliente": "Daniel",
        "importe": 275.60,
        "estado": "enviado"
    },
    {
        "numero": 110,
        "cliente": "Elena",
        "importe": 42.00,
        "estado": "entregado"
    },
    {
        "numero": 111,
        "cliente": "Miguel",
        "importe": 189.95,
        "estado": "cancelado"
    },
    {
        "numero": 112,
        "cliente": "Paula",
        "importe": 135.40,
        "estado": "pendiente"
    }
]


estados = {"pendiente","enviado", "entregado","cancelado"}


def añadir_pedido(pedido):
    for ped in pedidos:
        if ped['numero'] == pedido['numero']:
            print("El pedido ya existe")
            return

    pedidos.append(pedido)
    print("Pedido añadido")


def buscar_pedido(numero):

    for pedido in pedidos:
        if pedido['numero'] == numero:
            print(pedido)
            return

    print("El pedido no existe")


def cambiar_estado(numero,estado):

    for pedido in pedidos:
        if pedido['numero'] == numero and estado in estados:
            pedido['estado'] = estado
            return

    print("El pedido no existe")


def mostrar_pedidos_pendientes():
    for pedido in pedidos:
        if pedido['estado'] == 'pendiente':
            print(pedido)


def mostrar_pedidos_cliente(nombre):
     for pedido in pedidos:
        if pedido['cliente'] == nombre:
            print(pedido)
            return

     print("El cliente no existe")


def importe_total_pedidos():
    total = 0

    for pedido in pedidos:
        total += pedido['importe']

    print(f"TOTAL PEDIDOS: {total}")


def pedido_mayor_importe():
    pedido_mayor = {"importe":0}

    for pedido in pedidos:
        if pedido['importe'] > pedido_mayor['importe']:
            pedido_mayor = pedido

    print(f"MAYOR: {pedido_mayor}")


def mostrar_pedidos_estados():

    for estado in estados:
        cont = 0
        for pedido in pedidos:
            if pedido['estado'] == estado:
                cont+=1
        print(f"ESTADO {estado}, PEDIDOS: {cont}")


def main():

    while True:
        menu()
        op = int(input("Introduce una opcion: "))

        if op == 1:
            numero = int(input("Numero: "))
            cliente = input("Cliente: ")
            importe = int(input("Importe: "))
            estado = input("Estado: ")

            if estado not in estados:
                print("Estado no valido")
            else:
                pedido = {"numero": numero,"cliente": cliente,"importe": importe,"estado": estado}
                añadir_pedido(pedido)


        elif op == 2:
            numero = int(input("Numero: "))
            buscar_pedido(numero)

        elif op == 3:
            numero = int(input("Numero: "))
            estado = input("Estado: ")

            cambiar_estado(numero,estado)
            
        elif op == 4:
            mostrar_pedidos_pendientes()

        elif op == 5:
            nombre = input("Nombre del cliente: ")
            mostrar_pedidos_cliente(nombre)

        elif op == 6:
            importe_total_pedidos()

        elif op == 7:
            pedido_mayor_importe()

        elif op == 8:
            mostrar_pedidos_estados()

        elif op == 9:
            break



def menu():

    print("1. Registrar un nuevo pedido")
    print("2. Buscar un pedido por número")
    print("3. Cambiar el estado de un pedido")
    print("4. Mostrar todos los pedidos pendientes")
    print("5. Mostrar todos los pedidos de un determinado cliente")
    print("6. Calcular el importe total de los pedidos")
    print("7. Obtener el pedido de mayor importe")
    print("8. Mostrar cuántos pedidos existen en cada estado")
    print("9. Salir")


if __name__ == "__main__":
    main()