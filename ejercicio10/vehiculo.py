
class Vehiculo():
    def __init__(self, matricula,marca,modelo,precio_dia,disponible=True):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.precio_dia = precio_dia
        self.disponible = disponible

    def alquilar(self):

        if self.disponible:
            self.disponible = False
            return 
        print("El vehiculo esta alquilado")

    def devolver(self):
        self.disponible = True

    def mostrar_datos(self):
        return f"VEHICULO: {self.matricula} - MARCA: {self.marca} - MODELO: {self.modelo} - PRECIO DIA: {self.precio_dia} - DISPONIBLE: {self.disponible}"

    def calcular_precio(self,dias):
        return f"{dias * self.precio_dia}€"

    