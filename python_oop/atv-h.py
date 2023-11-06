# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add(self, item):
        self.cart.append(item)

    def remove(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                return

        raise Exception("Item not found")

    def total(self):
        total = 0

        for item in self.cart:
            total += item.price

        return total

    def __str__(self):
        string = ""

        for item in self.cart:
            string += f"{item.name} - {item.price}\n"

        return string


def main():
    try:
        shopping_cart = ShoppingCart()
        shopping_cart.add(Item("banana", 2.5))
        shopping_cart.add(Item("maça", 3.5))
        shopping_cart.add(Item("laranja", 4.5))
        shopping_cart.add(Item("pera", 5.5))
        print(shopping_cart)
        print("total: ", shopping_cart.total())
        shopping_cart.remove("banana")
        print(shopping_cart)
        print("total: ", shopping_cart.total())
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
