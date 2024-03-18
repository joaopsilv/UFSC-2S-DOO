from Pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, comissao: int, cpf: int, nome: str) -> None:
        super().__init__(cpf, nome)
        if isinstance(comissao, int):
            self.__comissao = comissao

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao: int):
        if isinstance(comissao, int):
            self.__comissao = comissao
