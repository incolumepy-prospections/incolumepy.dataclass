"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização basica de classes para estrutura de dados, com sobrescrita de
__str__. E se houver muitos campos torna complicado o gerenciamento.

algo do tipo:
    John, 123 Main St
"""


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.address}"


class NewPerson:
    def __init__(
        self,
        name: str,
        address: str,
        email: str,
        zip: str,
        city: str,
        coutry: str,
    ):
        self.name = name
        self.address = address
        self.email = (email,)
        self.zip = (zip,)
        self.city = (city,)
        self.coutry = coutry

    def __str__(self):
        return "{name}, {address}".format(**self.__dict__)


def main():
    person = Person(name="John", address="123 Main St")
    print(person)

    nperson = NewPerson(
        name="Joe", address="456 Main st", email="", zip="", city="", coutry=""
    )
    print(nperson)


if __name__ == "__main__":  # pragma: no cover
    main()
