from pessoa import Pessoa
from cargo import Cargo
from dependente import Dependente


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cargo: Cargo) -> None:
        super().__init__(nome, cpf)
        self.__cargo = None
        self.__dependentes = []
        if isinstance(cargo, Cargo):
            self.__cargo = cargo

    @property
    def cargo(self) -> Cargo:
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: Cargo):
        if isinstance(cargo, Cargo):
            self.__cargo = cargo

    def add_dependente(self, nome: str, cpf: str):
        if isinstance(nome, str) and isinstance(cpf, str):
            if self.__find_dependente_by_cpf(cpf) == None:
                self.__dependentes.append(Dependente(nome, cpf))

    def rem_dependente(self, cpf: str):
        if isinstance(cpf, str):
            dep = self.__find_dependente_by_cpf(cpf)
            if dep != None:
                self.__dependentes.remove(dep)

    def __find_dependente_by_cpf(self, cpf: str) -> Dependente:
        for dep in self.__dependentes:
            if dep.cpf == cpf:
                return dep

    def mostra_dados(self):
        super().mostra_dados()
        print("Cargo:", self.__cargo.titulo)
        print("Salário:", self.__cargo.salario)
