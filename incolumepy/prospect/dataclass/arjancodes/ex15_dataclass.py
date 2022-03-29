"""
This Is Why Python Data Classes Are Awesome

https://www.youtube.com/watch?v=CvQ7e6yUtnw

Utilização dataclass para estrutura de dados, torna o gerenciamento de campos
mais suave. Inclusive ao definir valores com padrão inicial.

Exemplos de performance com slots ativado ~30% de melhoria.

no_slots=0.1506832499981101
slots=0.10263681699871086
% performance improvement:  31.89%
"""
import dataclasses
from dataclasses import dataclass, field
import timeit
from functools import partial


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


# class PersonEmployee(PersonSlots, Person):
#     ...


def get_set_delete(person: Person | PersonSlots):
    person.address = '123 main st'
    a = person.address
    del person.address


def main():
    person = Person(name="John", address="123 Main St", email='john@jc.co')
    person_slots = PersonSlots(name="John", address="123 Main St", email='john@jc.co')
    no_slots = min(
        timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = min(
        timeit.repeat(partial(get_set_delete, person_slots), number=1000000))
    print(f'{no_slots=}')
    print(f'{slots=}')
    print(f'% performance improvement: {(no_slots - slots) / no_slots: .2%}')


if __name__ == "__main__":  # pragma: no cover
    main()
