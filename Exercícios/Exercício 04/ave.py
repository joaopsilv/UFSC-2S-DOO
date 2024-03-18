from abc import ABC, abstractmethod
from animal import Animal


class Ave(Animal, ABC):
    @abstractmethod
    def __init__(self, tamanho_passo: int, altura_voo: int) -> None:
        super().__init__(tamanho_passo)
        self.__altura_voo = None
        if isinstance(altura_voo, int):
            self.__altura_voo = altura_voo
    
    @property
    def altura_voo(self) -> int:
        return self.__altura_voo
    
    @altura_voo.setter
    def altura_voo(self, altura_voo: int):
        if isinstance(altura_voo, int):
            self.__altura_voo = altura_voo
         
    def mover(self) -> str:
        return super().mover() + " VOANDO"
    
    def produzir_som(self) -> str:
        return "AVE: PRODUZ SOM: PIU"
