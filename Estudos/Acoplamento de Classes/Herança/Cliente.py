from Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, endereco: str, cpf: int, nome: str):
        super().__init__(cpf, nome)
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco
