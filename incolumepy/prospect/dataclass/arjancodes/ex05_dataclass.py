"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave. Inclusive ao definir valores com padrão inicial.

E também gerencia estruturas complexas para valores iniciais.

algo do tipo:
    Person(name='John', address='123 Main St', actived=True, email_address=[], id='IIGIRYTQQZTL')
"""
from dataclasses import dataclass, field
from utils import generate_id


@dataclass
class Person:
    name: str
    address: str
    actived: bool = True
    email_address: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)


def main():
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == "__main__":  # pragma: no cover
    main()
