from funcionario import Funcionario


class Vendedor(Funcionario):
    def __init__(self, cpf: str, salario_base: float, comissao: float, total_vendas: float) -> None:
        super().__init__(cpf, salario_base)
        if isinstance(comissao, float):
            self.__comissao = comissao
        if isinstance(total_vendas, float):
            self.__total_vendas = total_vendas

    @property
    def comissao(self) -> float:
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao: float):
        if isinstance(comissao, float):
            self.__comissao = comissao

    @property
    def total_vendas(self) -> float:
        return self.__total_vendas

    @total_vendas.setter
    def total_vendas(self, total_vendas: float):
        if isinstance(total_vendas, float):
            self.__total_vendas = total_vendas

    def salario_total(self) -> float:
        return self.salario_base + (self.__total_vendas * self.__comissao / 100)
