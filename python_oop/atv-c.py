# Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations.


class Calculator:
    def __init__(self):
        pass

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pow(self, a, b):
        return a**b


def main():
    try:
        calculator = Calculator()
        print(calculator.sum(2, 2))
        print(calculator.sub(2, 2))
        print(calculator.mult(2, 2))
        print(calculator.div(2, 2))
        print(calculator.pow(2, 2))
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
