
from abc import ABC, abstractmethod


# Clase principal
class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


# Figura: Cuadrado
class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


# Figura: Rectangulo
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# Figura: Circulo
class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2


# Nueva figura: Triangulo
class Triangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


# Calculadora de areas
class CalculadoraAreas:

    def calcular(self, figura):
        return figura.calcular_area()


# Programa principal
calculadora = CalculadoraAreas()

cuadrado = Cuadrado(5)
rectangulo = Rectangulo(4, 6)
circulo = Circulo(3)
triangulo = Triangulo(6, 4)

print("Area del cuadrado:", calculadora.calcular(cuadrado))
print("Area del rectangulo:", calculadora.calcular(rectangulo))
print("Area del circulo:", calculadora.calcular(circulo))
print("Area del triangulo:", calculadora.calcular(triangulo))
