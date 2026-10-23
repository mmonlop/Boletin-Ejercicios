
class CuentaBancaria:
    def __init__(self,numero_cuenta,titular,saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def ingresar(self,cantidad):

        if cantidad <= 0:
            print("Cantidad no valida")
        else:
            self.saldo += cantidad

    def retirar(self,cantidad):

        if cantidad <= 0:
            print("Cantidad no valida")
            return

        if cantidad > self.saldo:
            print("No hay dinero")
        else:
            self.saldo -= cantidad


    def mostrar_saldo(self):
        return self.saldo

    def mostrar_datos(self):
        return f"NUMERO CUENTA: {self.numero_cuenta} - TITULAR: {self.titular} - SALDO: {self.saldo}"      

    def transferir(self,destino,cantidad):
        if self.saldo < cantidad:
            print("No hay dinero suficiente")
        else:
            self.saldo -= cantidad
            destino.saldo += cantidad