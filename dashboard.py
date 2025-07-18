import os
import subprocess

# CAMBIO 1:
# Nueva función para recorrer las carpetas llamadas "Tarea semana N"
# y buscar automáticamente archivos .py en su interior.
def listar_scripts_en_tareas(base_path):
    scripts = {}
    idx = 1
    for carpeta in sorted(os.listdir(base_path)):
        ruta_carpeta = os.path.join(base_path, carpeta)
        if os.path.isdir(ruta_carpeta) and carpeta.startswith("Tarea semana"):
            for archivo in os.listdir(ruta_carpeta):
                if archivo.endswith(".py"):
                    ruta_relativa = os.path.join(carpeta, archivo)
                    scripts[str(idx)] = ruta_relativa
                    idx += 1
    return scripts

# CAMBIO 2:
# Muestra el contenido del archivo seleccionado
def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except Exception as e:
        print(f"⚠️ Error al leer el archivo: {e}")

# CAMBIO 3:
# Permite ejecutar el script directamente desde el dashboard
def ejecutar_script(ruta_script):
    try:
        print(f"\n▶️ Ejecutando {ruta_script}...\n")
        subprocess.run(["python", ruta_script], check=True)
    except Exception as e:
        print(f"⚠️ Error al ejecutar: {e}")

# CAMBIO 4:
# Menú principal del dashboard mejorado, muestra scripts disponibles agrupados por carpeta
def mostrar_menu():
    base_dir = os.path.dirname(__file__)  # Ruta donde se encuentra dashboard.py
    scripts = listar_scripts_en_tareas(base_dir)  # Llama a la función que detecta scripts

    while True:
        print("\n📘 DASHBOARD - Programación Orientada a Objetos")
        for key, path in scripts.items():
            print(f"{key} - {path}")
        print("0 - Salir")

        eleccion = input("\nSelecciona un número o '0' para salir: ")
        if eleccion == '0':
            print("👋 Hasta luego.")
            break
        elif eleccion in scripts:
            ruta_script = os.path.join(base_dir, scripts[eleccion])

            # ✅ CAMBIO 5:
            # Se agregó un submenú para elegir si se desea mostrar o ejecutar el código
            print("\n¿Qué deseas hacer?")
            print("1 - Ver código fuente")
            print("2 - Ejecutar script")
            accion = input("Elige una opción: ")

            if accion == '1':
                mostrar_codigo(ruta_script)
            elif accion == '2':
                ejecutar_script(ruta_script)
            else:
                print("⚠️ Opción no válida.")
        else:
            print("⚠️ Entrada inválida. Intenta de nuevo.")

# CAMBIO 6:
# Se mantiene la estructura de ejecución habitual
if __name__ == "__main__":
    mostrar_menu()
