# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
from datetime import date, datetime


def date_str_converter(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Data de nascimento em formato inválido. Use yyyy-mm-dd.")


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        today = date.today()
        age = (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
        return age

    def __str__(self):
        return f"name: {self.name}\ncountry: {self.country}\ndate of birth: {self.date_of_birth}"


def main():
    try:
        name = input("digite o nome: ")
        country = input("digite o pais: ")
        date_of_birth_str = input("digite a data de nascimento (yyyy-mm-dd): ")
        date_of_birth = date_str_converter(date_of_birth_str)

        person = Person(name, country, date_of_birth)

        print(f"idade: {person.age()}")
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
