"Calculadora de áreas geométricas"

import math

def calcular_area_circulo(radio):
    "Calcula el área de un círculo dado el radio."
    return math.pi * radio ** 2

def calcular_area_rectangulo(base, altura):
    "Calcula el área de un rectángulo dada la base y la altura."
    return base * altura

def calcular_area_triangulo(base, altura):
    "Calcula el área de un triángulo dada la base y la altura."
    return (base * altura) / 2

def main():
    print("Bienvenido a la Calculadora de Áreas")
    print("Opciones: círculo, rectángulo, triángulo")

    figura = input("Introduce la figura que deseas calcular: ").lower()
    resultado_valido = True  # Tipo boolean

    if figura == "círculo" or figura == "circulo":
        radio = float(input("Introduce el radio del círculo: "))
        area = calcular_area_circulo(radio)
    elif figura == "rectángulo" or figura == "rectangulo":
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
    elif figura == "triángulo" or figura == "triangulo":
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
    else:
        print("Figura no reconocida.")
        resultado_valido = False

    if resultado_valido:
        print(f"El área del {figura} es: {area:.2f} unidades cuadradas.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
