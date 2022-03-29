"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave. Inclusive ao definir valores com padrão inicial.

Estruturas complexas com valores iniciais padrões, podem ser carregados na inicialização.

algo do tipo:
    Person(name='John', address='123 Main St', actived=False, email_address=[], id='IQCZLMHUHJEM')
    Person(name='John', address='123 Main St', actived=True, email_address=[], id='incolume1')
    Person(name='Joe', address='123 Main St', actived=True, email_address=['joe@incolumepy.com'], id='AHUYOWUVULJC')
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
    person = Person(name="John", address="123 Main St", actived=False)
    person1 = Person(name="John", address="123 Main St", id='incolume1')
    person2 = Person(
        name="Joe", address="123 Main St", email_address=['joe@incolumepy.com']
    )
    print(person, person1, person2, sep='\n')


if __name__ == "__main__":  # pragma: no cover
    main()
