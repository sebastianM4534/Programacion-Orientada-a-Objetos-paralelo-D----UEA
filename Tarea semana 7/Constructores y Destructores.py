class Archivo:
    def __init__(self, nombre_archivo, modo):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea una nueva instancia de la clase.
        Aquí abrimos un archivo y guardamos el objeto de archivo como atributo.
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = open(nombre_archivo, modo)
        print(f"Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        if 'w' in self.modo or 'a' in self.modo:
            self.archivo.write(texto + "\n")
            print("Texto escrito correctamente.")
        else:
            print("No se puede escribir en este archivo (modo lectura).")

    def leer(self):
        """
        Método para leer el contenido del archivo.
        """
        if 'r' in self.modo:
            contenido = self.archivo.read()
            print("Contenido del archivo:")
            print(contenido)
        else:
            print("No se puede leer este archivo (modo escritura).")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando se elimina el objeto o termina el programa.
        Aquí cerramos el archivo como forma de limpieza.
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


# --- Ejemplo de uso ---
print("Inicio del programa")

# Crear un objeto de tipo Archivo
archivo1 = Archivo("ejemplo.txt", "w")  # Abrimos el archivo en modo escritura
archivo1.escribir("Hola, este es un ejemplo de uso de __init__ y __del__ en Python.")

# Eliminamos manualmente el objeto para activar el destructor
del archivo1

print("Fin del programa")
