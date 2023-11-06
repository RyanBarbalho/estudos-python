# Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return self.stack

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


def main():
    try:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        print(stack)
        print("pop")
        print(stack.pop())
        print(stack)
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
