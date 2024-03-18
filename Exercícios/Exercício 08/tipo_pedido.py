

class TipoPedido():
    def __init__(self, descricao: str, fator_distancia: float):
        self.__descricao = None
        self.__fator_distancia = None
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(fator_distancia, float):
            self.__fator_distancia = fator_distancia

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def fator_distancia(self) -> float:
        return self.__fator_distancia

    @fator_distancia.setter
    def fator_distancia(self, fator_distancia):
        if isinstance(fator_distancia, float):
            self.__fator_distancia = fator_distancia
