from pessoa import Pessoa
from professor import Professor


class Aluno(Pessoa):
    def __init__(self, matricula: int, nome: str, endereco: str, orientador: Professor):
        super().__init__(nome, endereco)
        if isinstance(matricula, int):
            self.__matricula = matricula
        else:
            raise ValueError("A matrícula de um aluno precisa ser tipada como um inteiro!")
        if isinstance(orientador, Professor):
            self.__orientador = orientador
        else:
            raise ValueError("O orientador de um aluno precisa ser um Professor!")

    @property
    def matricula(self) -> int:
        return self.__matricula
  
    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula
        else:
            raise ValueError("A matrícula de um aluno precisa ser tipada como um inteiro!")
        
    @property
    def orientador(self) -> Professor:
        return self.__orientador
    
    @orientador.setter
    def orientador(self, orientador: Professor):
        if isinstance(orientador, Professor):
            self.__orientador = orientador
        else:
            raise ValueError("O orientador de um aluno precisa ser um Professor!")
