from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = None
        self.__total_passageiros = None
        self.__ligado = None
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
        if isinstance(total_passageiros, int):
            self.__total_passageiros = total_passageiros
        if isinstance(ligado, bool):
            self.__ligado = ligado

    def ligar(self) -> str:
        if self.__ligado is True:
            raise OnibusJahLigadoException
        else:
            self.__ligado = True
            return "Onibus ligado"

    def desligar(self) -> str:
        if self.__ligado is False:
            raise OnibusJahDesligadoException
        else:
            self.__ligado = False
            return "Onibus desligado"

    def embarca_pessoa(self) -> str:
        if self.__total_passageiros == self.__capacidade:
            raise OnibusJahCheioException
        else:
            self.__total_passageiros += 1
            return "Passageiro embarcado"

    def desembarca_pessoa(self) -> str:
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException
        else:
            self.__total_passageiros -= 1
            return "Passageiro desembarcado"

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    @property
    def ligado(self) -> bool:
        return self.__ligado

    @capacidade.setter
    def capacidade(self, capacidade: int):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
