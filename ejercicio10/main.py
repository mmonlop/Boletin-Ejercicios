from vehiculo import Vehiculo
from EmpresaAlquiler import EmpresaAlquiler



def main():
    
    empresa = EmpresaAlquiler()

    while True:
        menu()
        op = int(input("Introduce una opcion: "))

        if op == 1:
            matricula = input("Matricula: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            precio_dia = int(input("Precio dia: "))

            vehiculo = Vehiculo(matricula,marca,modelo,precio_dia)

            empresa.añadir_vehiculo(vehiculo)

        elif op == 2:
            empresa.listar_vehiculos()

        elif op == 3:
            empresa.vehiculos_disponibles()

        elif op == 4:
            vehiculo_a_alquilar = {}
            
            matricula = input("Matricula: ")            

            for coche in empresa.vehiculos:
                if matricula == coche.matricula:
                    vehiculo_a_alquilar = coche

            empresa.alquilar_vehiculo(vehiculo_a_alquilar)

        elif op == 5:
            vehiculo_a_devolver = {}
            
            matricula = input("Matricula: ")            

            for coche in empresa.vehiculos:
                if matricula == coche.matricula:
                    vehiculo_a_devolver = coche

            empresa.devolver_vehiculo(vehiculo_a_devolver)


        elif op == 6:
            vehiculo_a_consultar = None

            matricula = input("Matricula: ")            
            dias = int(input("Dias: "))

            for coche in empresa.vehiculos:
                if matricula == coche.matricula:
                    vehiculo_a_consultar = coche

            if vehiculo_a_consultar is not None:
                print(empresa.calcular_alquiler(dias,vehiculo_a_consultar))
            else:
                print("El vehiculo no existe")
        elif op == 7:
            break


def menu():
    print("1. Añadir vehiculo")
    print("2. Mostrar vehiculos")
    print("3. Mostrar vehiculos disponibles")
    print("4. Alquilar vehiculo")
    print("5. Devolver vehiculo")
    print("6. Consultar precio de alquiler")
    print("7. Salir")

if __name__ == "__main__":
    main()