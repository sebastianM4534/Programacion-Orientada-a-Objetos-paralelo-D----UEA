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

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"

    # Representación para guardar en archivo

    def to_file(self):
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}"

    # Crear producto a partir de una línea de archivo

    @staticmethod
    def from_file(linea):
        try:
            id_producto, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            return None  # Si la línea está corrupta

# CLASE INVENTARIO

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []          # Lista de productos en memoria
        self.archivo = archivo       # Archivo donde se guarda el inventario
        self.cargar_desde_archivo()  # Se reconstruye el inventario desde el archivo

    # Cargar inventario desde archivo

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    producto = Producto.from_file(linea)
                    if producto:
                        self.productos.append(producto)
            print(f"Inventario cargado desde {self.archivo}.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará automáticamente al guardar.")
        except PermissionError:
            print(f"Error: No tienes permiso para leer el archivo {self.archivo}.")

    # Guardar inventario en archivo (reescribe todo el archivo)

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(p.to_file() + "\n")
            print(f"Inventario guardado en {self.archivo}.")
        except PermissionError:
            print(f"Error: No tienes permiso para escribir en el archivo {self.archivo}.")

    # Añadir nuevo producto

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    # Eliminar producto por ID

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    # Actualizar producto

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    # Buscar por nombre

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar inventario

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

# MENÚ

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
    inventario = Inventario()  # Al iniciar, carga desde archivo

    while True:
        opcion = menu()

        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: La cantidad debe ser un número entero y el precio un número decimal.")

        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (dejar vacío si no desea cambiar): ")
            precio = input("Ingrese nuevo precio (dejar vacío si no desea cambiar): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Formato de número incorrecto.")

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# EJECUCIÓN DEL PROGRAMA

if __name__ == "__main__":
    main()
