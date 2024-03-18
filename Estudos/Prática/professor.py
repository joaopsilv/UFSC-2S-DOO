from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, id_funcionario: int, nome: str, endereco: str, telefone: str):
        super().__init__(nome, endereco)
        if isinstance(id_funcionario, int):
            self.__id_funcionario = id_funcionario
        else:
            raise ValueError("O id de um funcionário precisa ser tipado como um inteiro!")
        if isinstance(telefone, str):
            self.__telefone = telefone
        else:
            raise ValueError("Telefone precisa ser tipado como uma string!")
        
    @property
    def id_funcionario(self) -> int:
        return self.__id_funcionario
  
    @id_funcionario.setter
    def id_funcionario(self, id_funcionario: int):
        if isinstance(id_funcionario, int):
            self.__id_funcionario = id_funcionario
        else:
            raise ValueError("O id de um funcionário precisa ser tipado como um inteiro!")
    
    @property
    def telefone(self) -> str:
        return self.__telefone
  
    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone
        else:
            raise ValueError("telefone precisa ser tipado como uma string!")
        