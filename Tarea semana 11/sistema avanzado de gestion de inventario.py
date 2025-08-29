import json

# Clase Producto

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

# Clase Inventario

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario {id: Producto}
        self.cargar()

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("⚠ El ID ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar()
            print("✔ Producto agregado correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar()
            print("✔ Producto eliminado.")
        else:
            print("⚠ No se encontró el producto con ese ID.")

    def actualizar_cantidad(self, id, nueva_cantidad):
        if id in self.productos:
            self.productos[id].cantidad = nueva_cantidad
            self.guardar()
            print("✔ Cantidad actualizada.")
        else:
            print("⚠ No se encontró el producto.")

    def actualizar_precio(self, id, nuevo_precio):
        if id in self.productos:
            self.productos[id].precio = nuevo_precio
            self.guardar()
            print("✔ Precio actualizado.")
        else:
            print("⚠ No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"[{p.id}] {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")
        else:
            print("⚠ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("⚠ El inventario está vacío.")
        else:
            for p in self.productos.values():
                print(f"[{p.id}] {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=2)

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = {d["id"]: Producto.from_dict(d) for d in data}
        except FileNotFoundError:
            self.productos = {}

# Menú de consola

def menu():
    inventario = Inventario()

    while True:
        print("\n=== MENÚ INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)

        elif opcion == "4":
            id = input("ID del producto: ")
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id, precio)

        elif opcion == "5":
            nombre = input("Nombre del producto: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "6":
            inventario.mostrar_todos()

        elif opcion == "0":
            print("Saliendo... ¡Hasta pronto!")
            break

        else:
            print("⚠ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
