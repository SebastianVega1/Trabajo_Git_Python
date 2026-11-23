import math

def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2


print("CALCULO DE AREAS")
figura = input("Ingrese la figura (cuadrado, rectangulo o circulo): ").lower()

if figura == "cuadrado":
    lado = float(input("Ingrese el lado: "))
    print("Area:", calcular_area_cuadrado(lado))

elif figura == "rectangulo":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    print("Area:", calcular_area_rectangulo(base, altura))

elif figura == "circulo":
    radio = float(input("Ingrese el radio: "))
    print("Area:", calcular_area_circulo(radio))

else:
    print("Figura no valida")