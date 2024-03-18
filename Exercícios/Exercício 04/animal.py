from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, tamanho_passo: int) -> None:
        self.__tamanho_passo = None
        if isinstance(tamanho_passo, int):
            self.__tamanho_passo = tamanho_passo
    
    @property
    def tamanho_passo(self) -> int:
        return self.__tamanho_passo
    
    @tamanho_passo.setter
    def tamanho_passo(self, tamanho_passo: int):
        if isinstance(tamanho_passo, int):
            self.__tamanho_passo = tamanho_passo
    
    def mover(self) -> str:
        return "ANIMAL: DESLOCOU " + str(self.__tamanho_passo)
    
    @abstractmethod
    def produzir_som():
        pass
