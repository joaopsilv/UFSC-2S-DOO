from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    @abstractmethod
    def __init__(self, nome: str, codigo: int) -> None:
        self.__nome = None
        self.__codigo = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def codigo(self) -> int:
        return self.__codigo
