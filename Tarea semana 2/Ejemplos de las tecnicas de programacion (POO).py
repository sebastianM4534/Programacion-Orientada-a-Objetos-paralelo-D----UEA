# Ejemplo de Abstraccion (sistema de pagos)

from abc import ABC, abstractmethod

#define la interfaz general de un método de pago

class MetodoDePago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass
#tarjeta de crédito
class TarjetaCredito(MetodoDePago):
    def __init__(self, titular):
        self.titular = titular

    def pagar(self, monto):
        print(f"{self.titular} pagó ${monto:.2f} con tarjeta de crédito.")

# PayPal
class PayPal(MetodoDePago):
    def __init__(self, email):
        self.email = email

    def pagar(self, monto):
        print(f"Se realizó un pago de ${monto:.2f} vía PayPal desde {self.email}.")

def procesar_pago(metodo, monto):
    metodo.pagar(monto)

procesar_pago(TarjetaCredito("Ana Torres"), 150.75)
procesar_pago(PayPal("ana.torres@mail.com"), 89.99)



# Ejemplo de Encapsulamiento (cuenta bancaria)

class Cuenta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso de ${cantidad:.2f}")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad:.2f}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def ver_saldo(self):
        return f"Saldo de {self.titular}: ${self.__saldo:.2f}"

cuenta = Cuenta("Carlos Ramírez", 500)
cuenta.depositar(300)
cuenta.retirar(200)
print(cuenta.ver_saldo())


# ejemplo de Herencia (sistema de empleados)

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        return f"{self.nombre} está trabajando."

class Desarrollador(Empleado):
    def trabajar(self):
        return f"{self.nombre} está escribiendo código en Python."

class Diseñador(Empleado):
    def trabajar(self):
        return f"{self.nombre} está diseñando interfaces de usuario."

equipo = [Desarrollador("Lucía"), Diseñador("Mateo")]

for miembro in equipo:
    print(miembro.trabajar())


# Ejemplo de polimorfismo (animaciones de una interfaz)

class ComponenteUI:
    def animar(self):
        pass

class Boton(ComponenteUI):
    def animar(self):
        return "Botón se desliza desde la derecha."

class Menu(ComponenteUI):
    def animar(self):
        return "Menú aparece con efecto de desvanecimiento."

class Imagen(ComponenteUI):
    def animar(self):
        return "Imagen gira en 3D."

# Función polimórfica
def mostrar_animacion(componente):
    print(componente.animar())

elementos = [Boton(), Menu(), Imagen()]

for elemento in elementos:
    mostrar_animacion(elemento)
