

class Pessoa:
    def __init__(self, nome: str, endereco: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Nome precisa ser tipado como uma string!")
        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            raise ValueError("Endereço precisa ser tipado como uma string!")

    @property
    def nome(self) -> str:
        return self.__nome
  
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Nome precisa ser tipado como uma string!")
            
    @property
    def endereco(self) -> str:
        return self.__endereco
  
    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            raise ValueError("Endereço precisa ser tipado como uma string!")
