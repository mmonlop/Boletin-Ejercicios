
class EmpresaAlquiler:
    def __init__(self):
       self.vehiculos = []

    def añadir_vehiculo(self,vehiculo):

        for vehic in self.vehiculos:
            if vehic.matricula == vehiculo.matricula:
                print("El vehiculo ya existe")
                return
        
        self.vehiculos.append(vehiculo)
        print("Vehiculo añadido")

    def buscar_vehiculo(self,matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula  ==  matricula:
                return vehiculo.mostrar_datos()

        return f"El vehiculo no existe"

    def listar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.mostrar_datos())

    def vehiculos_disponibles(self):
        for vehiculo in self.vehiculos:
            if vehiculo.disponible: 
                print(vehiculo.mostrar_datos())

    def alquilar_vehiculo(self,vehiculo):
        if vehiculo not in self.vehiculos:
            print("El vehiculo no existe")
            return

        if not vehiculo.disponible:
            print("Vehiculo no disponible")
            return
        
        vehiculo.disponible = False
        print("Vehiculo alquilado correctamente")

    def devolver_vehiculo(self,vehiculo):
       
        if vehiculo not in self.vehiculos:
            print("El vehiculo no existe")
            return

        if vehiculo.disponible:
            print("Vehiculo disponible")
            return

        
        vehiculo.disponible = True
        print("Vehiculo devuelto correctamente")


    def calcular_alquiler(self,dias,vehiculo):
        return f"ALQUILER POR {dias} DIAS: {vehiculo.precio_dia * dias}€"


    def vehiculo_precio_alto(self):
        prcio_mas_alto = 0

        for vehiculo in self.vehiculos:
            if vehiculo.precio_dia > prcio_mas_alto:
                prcio_mas_alto = vehiculo.precio_dia

        return f"PRECIO MAS ALTO: {prcio_mas_alto}"