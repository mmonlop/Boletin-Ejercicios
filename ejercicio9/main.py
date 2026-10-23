from CuentaBancaria import CuentaBancaria


def main():

    cuentas = []

    #Crea al menos 5 cuentas bancarias.
    c1 = CuentaBancaria("C001","Manuel", 200)
    c2 = CuentaBancaria("C002", "Lucía", 350)
    c3 = CuentaBancaria("C003", "Antonio", 500)
    c4 = CuentaBancaria("C004", "Marta", 275)
    c5 = CuentaBancaria("C005", "Sergio", 420)

    #Almacénalas en una lista.
    cuentas.append(c1)
    cuentas.append(c2)
    cuentas.append(c3)
    cuentas.append(c4)
    cuentas.append(c5)

    #Realiza diferentes ingresos y retiradas

    c1.ingresar(500)
    c3.ingresar(100)
    c2.retirar(50)
    c5.ingresar(50)


    #Muestra los datos de todas las cuentas.
    for cuenta in cuentas:
        print(cuenta.mostrar_datos())

    #Obtén la cuenta con mayor saldo

    mayor_saldo = 0
    cuenta_mas_saldo = {}
    for cuenta in cuentas:
        if cuenta.mostrar_saldo() > mayor_saldo:
            mayor_saldo = cuenta.mostrar_saldo()
            cuenta_mas_saldo = cuenta

    print(f"CUENTA CON MAYOR SALDO: ")
    print(cuenta_mas_saldo.mostrar_datos())


    #Calcula el dinero total almacenado entre todas las cuentas

    total_cuentas = 0

    for cuenta in cuentas:
        total_cuentas += cuenta.mostrar_saldo()

    print(f"Total de dinero: {total_cuentas}")



    #Ampliación (Transferir)

    c1.transferir(c2,100)

    for cuenta in cuentas:
        print(cuenta.mostrar_datos())



if __name__ == "__main__":
    main()