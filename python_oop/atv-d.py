# Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square.

from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        area = 3.14 * (self.raio**2)
        return f"area do circulo: {area}"

    def perimeter(self):
        perimetro = 2 * 3.14 * self.raio
        return f"perimetro do circulo: {round(perimetro, 2)}"


class Triangle(Shape):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        semiperimetro = (self.lado1 + self.lado2 + self.lado3) / 2
        area = sqrt(
            semiperimetro
            * (semiperimetro - self.lado1)
            * (semiperimetro - self.lado2)
            * (semiperimetro - self.lado3)
        )
        return f"area do triangulo: {area}"

    def perimeter(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return f"perimetro do triangulo: {perimetro}"


class Square(Shape):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        area = self.lado**2
        return f"area do quadrado: {area}"

    def perimeter(self):
        perimetro = 4 * self.lado
        return f"perimetro do quadrado: {perimetro}"


def main():
    try:
        print("circulo")
        raio = 5
        circulo = Circle(raio)
        print(circulo.area())
        print(circulo.perimeter())

        print("\ntriangulo")
        lado1 = 2
        lado2 = 3
        lado3 = 4
        triangulo = Triangle(lado1, lado2, lado3)
        print(triangulo.area())
        print(triangulo.perimeter())

        print("\nquadrado")
        lado = 8
        quadrado = Square(lado)
        print(quadrado.area())
        print(quadrado.perimeter())
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
