"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave.

algo do tipo:
    Person(name='John', address='123 Main St')
"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    address: str


def main():
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == "__main__":  # pragma: no cover
    main()
