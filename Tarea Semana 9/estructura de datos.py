
# CLASE PRODUCTO

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad disponible
        self._precio = precio  # Precio unitario

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Representación del producto como string
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
# CLASE INVENTARIO

class Inventario:
    def __init__(self):
        self.productos = []  # Lista que almacenará los productos

    # Añadir nuevo producto, verificando que el ID sea único
    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    # Actualizar cantidad o precio de un producto por ID
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    # Buscar productos por nombre (puede haber nombres similares)
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

# FUNCIONES DEL MENÚ

def menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")

# PROGRAMA PRINCIPAL

def main():
    inventario = Inventario()  # Crear un inventario vacío

    while True:
        opcion = menu()

        if opcion == '1':
            # Agregar producto
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            # Eliminar producto
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            # Actualizar producto
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (dejar vacío si no desea cambiar): ")
            precio = input("Ingrese nuevo precio (dejar vacío si no desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            # Buscar producto por nombre
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            # Mostrar todos los productos
            inventario.mostrar_productos()

        elif opcion == '6':
            # Salir del programa
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# EJECUCIÓN DEL PROGRAMA


if __name__ == "__main__":
    main()
