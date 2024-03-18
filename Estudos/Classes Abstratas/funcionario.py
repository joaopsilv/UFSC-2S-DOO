from abc import ABC, abstractmethod


class Funcionario(ABC):
    @abstractmethod
    def __init__(self, cpf: str, salario_base: float) -> None:
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(salario_base, float):
            self.__salario_base = salario_base

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base: float):
        if isinstance(salario_base, float):
            self.__salario_base = salario_base

    @abstractmethod
    def salario_total(self) -> float:
        pass
