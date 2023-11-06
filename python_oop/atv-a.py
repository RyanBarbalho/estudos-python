# Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.


class Circle:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        area = 3.14 * (self.raio**2)
        return f"area do circulo: {area}"

    def perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        return f"perimetro do circulo: {round(perimetro, 2)}"


def main():
    try:
        raio = float(input("digite o raio: "))
        circulo = Circle(raio)
        print(circulo.area())
        print(circulo.perimetro())
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
