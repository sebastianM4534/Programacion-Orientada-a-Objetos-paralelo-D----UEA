# Clase de una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero          # Número de habitación
        self.tipo = tipo              # Tipo: simple, doble, suite
        self.precio = precio          # Precio por noche
        self.ocupada = False          # Estado de la habitación

    def mostrar_info(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Estado: {estado}")


# Clase de una reserva de una habitacion
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion
        habitacion.ocupada = True  # Al hacer la reserva, la habitación se marca como ocupada

    def cancelar(self):
        print(f"Cancelando la reserva de {self.cliente} en la habitación {self.habitacion.numero}")
        self.habitacion.ocupada = False


# Clase del hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print(f"\nHabitaciones en el Hotel {self.nombre}:")
        for h in self.habitaciones:
            h.mostrar_info()

    def habitaciones_disponibles(self):
        return [h for h in self.habitaciones if not h.ocupada]

    def hacer_reserva(self, cliente, tipo_deseado):
        disponibles = [h for h in self.habitaciones_disponibles() if h.tipo == tipo_deseado]
        if disponibles:
            habitacion = disponibles[0]
            reserva = Reserva(cliente, habitacion)
            self.reservas.append(reserva)
            print(f"Reserva confirmada para {cliente} en la habitación {habitacion.numero}")
        else:
            print(f"No hay habitaciones {tipo_deseado} disponibles para {cliente}.")

    def cancelar_reserva(self, cliente):
        for reserva in self.reservas:
            if reserva.cliente == cliente:
                reserva.cancelar()
                self.reservas.remove(reserva)
                return
        print(f"No se encontró una reserva a nombre de {cliente}.")

# Crear hotel
mi_hotel = Hotel("Sol y Luna")

# Agregar habitaciones
mi_hotel.agregar_habitacion(Habitacion(101, "simple", 50))
mi_hotel.agregar_habitacion(Habitacion(102, "doble", 80))
mi_hotel.agregar_habitacion(Habitacion(103, "suite", 120))
mi_hotel.agregar_habitacion(Habitacion(104, "doble", 80))

# Mostrar habitaciones
mi_hotel.mostrar_habitaciones()

# Realizar reservas
mi_hotel.hacer_reserva("Juan Pérez", "doble")
mi_hotel.hacer_reserva("María López", "suite")
mi_hotel.hacer_reserva("Carlos Ruiz", "doble")  # Solo hay dos dobles

# Mostrar estado después de reservas
mi_hotel.mostrar_habitaciones()

# Cancelar una reserva
mi_hotel.cancelar_reserva("Juan Pérez")

# Mostrar estado final
mi_hotel.mostrar_habitaciones()
