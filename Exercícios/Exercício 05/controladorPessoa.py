from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        if self.__buscar_cliente(codigo) is None:
            cliente = Cliente(nome, codigo)
            self.__clientes.append(cliente)
            return cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        if self.__buscar_tecnico(codigo) is None:
            tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(tecnico)
            return tecnico

    def __buscar_cliente(self, codigo: int) -> Cliente:
        for cliente in self.__clientes:
            if cliente.codigo == codigo:
                return cliente

    def __buscar_tecnico(self, codigo: int) -> Tecnico:
        for tecnico in self.__tecnicos:
            if tecnico.codigo == codigo:
                return tecnico
