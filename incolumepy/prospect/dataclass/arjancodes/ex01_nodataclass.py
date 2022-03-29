"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização basica de classes para estrutura de dados, não é funcional
algo do tipo:
    <__main__.Person object at 0x7fa32889be80>
"""


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


def main():
    person = Person(name='John', address='123 Main St')
    print(person)


if __name__ == '__main__':    # pragma: no cover
    main()
