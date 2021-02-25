"""
    Por que usar Type Hints
    - Um dos principais objetivos, senao o principal, 
    e que o type hints ou type annotations facilita 
    a leitura do codigo para outros desenvolvedores
"""

from typing import List, Tuple, Dict, Any, Union, Sequence

# Tipos primitivos
inteiro: int = 10
floating: float = 10.2
string: str = 'Texto'
boolean: bool = True

# sequencias
lista_inteiros: List[int] = [10, 20, 30]
lista_string: List[str] = ["Fernando", "Luiz"]
lista_mista_str_int: List[Union[str, int]] = [1, 2, 3, 4, "Luiz"]
tupla: Tuple[int, int, str] = (10, 10, "Fernando")


p1: Dict[str, Union[str, int]] = {
    "nome"  : "Fernando Luiz",
    "email" : "s4antosf3rnando@gmail.com",
    "idade" : 18,
}


def retorna_nome_completo(nome: str, sobrenome: str) -> str:
    return f'{nome} {sobrenome}'


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade


def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]

print(iterar((1, 2, 3)))
