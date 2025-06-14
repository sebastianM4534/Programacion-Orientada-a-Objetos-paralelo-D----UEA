#Programacion Tradicional
# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("=== Programa Tradicional ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

main()

#programacion orientada a objetos (POO)

# Clase base para representar el clima de un día
class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.__dia = dia                      # Encapsulamiento del atributo
        self.__temperatura = temperatura

    def obtener_temperatura(self):
        return self.__temperatura

    def obtener_dia(self):
        return self.__dia

    def __str__(self):
        return f"{self.__dia}: {self.__temperatura}°C"

# Clase hija que podría usarse para agregar características futuras (Herencia)
class ClimaExtendido(ClimaDiario):
    def __init__(self, dia, temperatura, humedad=0):
        super().__init__(dia, temperatura)
        self.__humedad = humedad  # Atributo adicional

    def obtener_humedad(self):
        return self.__humedad

# Clase principal que gestiona toda la semana
class ClimaSemanal:
    def __init__(self):
        self.dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        self.registros = []

    def ingresar_datos(self):
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.registros.append(ClimaDiario(dia, temp))

    def calcular_promedio(self):
        total = sum(d.obtener_temperatura() for d in self.registros)
        return total / len(self.registros)

    def mostrar_registros(self):
        for registro in self.registros:
            print(registro)

# Función principal
def main():
    print("\n=== Programa con POO ===")
    semana = ClimaSemanal()
    semana.ingresar_datos()
    semana.mostrar_registros()
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

main()
