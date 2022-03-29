"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave. Inclusive ao definir valores com padrão inicial.

O decorador dataclass, possui parametros que modificam seu comportamento.
O parametro kw_only restringe a utilização de argumentos posicionais,
força utilização kwargs.

algo do tipo:
    TypeError Person.__init__() takes 1 positional argument but 3 were given

"""
import dataclasses
from dataclasses import dataclass, field
from utils import generate_id


@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    actived: bool = True
    email_address: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        """Metodo post init."""
        self._search_string = f'{self.name} {self.address}'


def main():
    try:
        person = Person(name="John", address="123 Main St")
        print(person)
        p = Person('Joe', '123 Secund st')
        print(p)
    except (TypeError, dataclasses.FrozenInstanceError) as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":  # pragma: no cover
    main()
