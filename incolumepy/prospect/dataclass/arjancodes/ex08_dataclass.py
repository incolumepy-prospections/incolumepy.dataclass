"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave. Inclusive ao definir valores com padrão inicial.

Os campos de inicialização bloqueados podem ser preenchido post_init.

algo do tipo:
    Person(
       name='John', address='123 Main St', actived=True, email_address=[],
       id='IRPLBUMXIARO', search_string='John 123 Main St'
    )

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
    search_string: str = field(init=False)

    def __post_init__(self):
        """Metodo post init."""
        self.search_string = f'{self.name} {self.address}'


def main():
    try:
        person = Person(name="John", address="123 Main St")
        print(person)
    except TypeError as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":  # pragma: no cover
    main()
