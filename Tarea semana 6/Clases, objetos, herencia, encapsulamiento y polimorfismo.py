# Clase base que representa a un empleado
class Empleado:
    def __init__(self, nombre, salario):
        # Encapsulación: atributo que es privado
        self.__nombre = nombre
        self.__salario = salario
    # Métodos para acceder y modificar el nombre (getter y setter)
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    # Método general que será sobrescrito en la clase derivada
    def mostrar_informacion(self):
        print(f"Empleado: {self.__nombre}, Salario: ${self.__salario:.2f}")

    # Otro método que puede usarse en polimorfismo
    def calcular_bono(self, porcentaje):
        return self.__salario * (porcentaje / 100)

# Clase derivada que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        # Llama al constructor de la clase base
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Polimorfismo: sobrescribimos el método de la clase base
    def mostrar_informacion(self):
        print(f"Gerente: {self.get_nombre()}, Departamento: {self.departamento}")

    # Polimorfismo con argumentos adicionales
    def calcular_bono(self, porcentaje, extra=0):
        # Utiliza el método base y le añade un bono extra
        bono_base = super().calcular_bono(porcentaje)
        return bono_base + extra
# Programa principal que demuestra la funcionalidad
if __name__ == "__main__":
    # Crear una instancia de Empleado
    empleado1 = Empleado("Carlos Pérez", 1200.00)
    empleado1.mostrar_informacion()

    # Crear una instancia de Gerente (clase derivada)
    gerente1 = Gerente("Ana Torres", 2500.00, "Finanzas")
    gerente1.mostrar_informacion()

    # Mostrar uso del método sobrescrito y encapsulación
    print(f"Nombre del empleado (encapsulado): {empleado1.get_nombre()}")
    empleado1.set_nombre("Carlos P.")
    print(f"Nombre actualizado: {empleado1.get_nombre()}")

    # Polimorfismo: uso del mismo método con diferentes comportamientos
    print(f"Bono de empleado: ${empleado1.calcular_bono(10):.2f}")
    print(f"Bono de gerente: ${gerente1.calcular_bono(10, 200):.2f}")
