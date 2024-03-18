from pessoa import Pessoa


class Dependente(Pessoa):
    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome, cpf)
        
    def mostra_dados(self):
        return super().mostra_dados()
