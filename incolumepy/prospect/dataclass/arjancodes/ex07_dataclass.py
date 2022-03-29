"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave. Inclusive ao definir valores com padrão inicial.

Os campos de inicialização também podem ser bloqueados para impedir modificação.

algo do tipo:
    person = Person(name="John", address="123 Main St", id='incolume1')
    TypeError Person.__init__() got an unexpected keyword argument 'id'
"""
from dataclasses import dataclass, field
from utils import generate_id


@dataclass
class Person:
    name: str
    address: str
    actived: bool = True
    email_address: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)


def main():
    try:
        person = Person(name="John", address="123 Main St", id='incolume1')
    except TypeError as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":  # pragma: no cover
    main()
