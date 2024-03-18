from dao import DAO
from cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self) -> None:
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            super().add(cliente.codigo, cliente)

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            return super().remove(codigo)
