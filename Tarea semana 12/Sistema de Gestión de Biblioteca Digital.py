
# Sistema de Gestión de Biblioteca Digital

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"[{self.isbn}] {self.info[0]} - {self.info[1]} ({self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}      # ISBN -> Libro
        self.usuarios = {}    # ID -> Usuario
        self.user_ids = set() # IDs únicos

    #Gestión de libros
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("⚠️ El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"✅ Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("⚠️ No se encontró el libro.")

    # Gestión de usuarios
    def registrar_usuario(self, usuario):
        if usuario.user_id in self.user_ids:
            print("⚠️ El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.user_ids.add(usuario.user_id)
            print(f"✅ Usuario registrado: {usuario}")

    def baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.user_ids.remove(user_id)
            print(f"✅ Usuario con ID {user_id} dado de baja.")
        else:
            print("⚠️ Usuario no encontrado.")

    # Gestión de préstamos
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("⚠️ Libro no disponible.")
            return

        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return

        usuario = self.usuarios[user_id]
        libro_devuelto = None

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_devuelto = libro
                break

        if libro_devuelto:
            usuario.libros_prestados.remove(libro_devuelto)
            self.libros[isbn] = libro_devuelto
            print(f"✅ Libro devuelto: {libro_devuelto}")
        else:
            print("⚠️ El usuario no tiene ese libro prestado.")

    # Búsqueda de libros
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Listar libros prestados
    def listar_libros_prestados(self, user_id):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return
        usuario = self.usuarios[user_id]
        if not usuario.libros_prestados:
            print(f"ℹ️ {usuario.nombre} no tiene libros prestados.")
        else:
            print(f"📚 Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f" - {libro}")


# Menú Interactivo
def menu():
    biblio = Biblioteca()

    # --- Datos precargados ---
    libros_demo = [
        Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1001"),
        Libro("1984", "George Orwell", "Distopía", "1002"),
        Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "1003"),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "1004")
    ]
    usuarios_demo = [
        Usuario("Sebastián", "U001"),
        Usuario("Ana", "U002"),
        Usuario("Carlos", "U003")
    ]

    for libro in libros_demo:
        biblio.agregar_libro(libro)

    for usuario in usuarios_demo:
        biblio.registrar_usuario(usuario)

    # Menú principal
    while True:
        print("\n====== 📚 MENÚ BIBLIOTECA DIGITAL ======")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblio.agregar_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblio.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID de usuario: ")
            biblio.registrar_usuario(Usuario(nombre, user_id))

        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            biblio.baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblio.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblio.devolver_libro(user_id, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input("Valor de búsqueda: ")
            resultados = biblio.buscar_libros(criterio, valor)
            if resultados:
                print("🔎 Resultados de la búsqueda:")
                for r in resultados:
                    print(" -", r)
            else:
                print("⚠️ No se encontraron resultados.")

        elif opcion == "8":
            user_id = input("ID del usuario: ")
            biblio.listar_libros_prestados(user_id)

        elif opcion == "9":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")


# EJECUTAR PROGRAMA
if __name__ == "__main__":
    menu()
