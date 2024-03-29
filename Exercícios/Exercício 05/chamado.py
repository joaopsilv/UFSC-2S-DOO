from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        self.__data = None
        self.__cliente = None
        self.__tecnico = None
        self.__titulo = None
        self.__descricao = None
        self.__prioridade = None
        self.__tipo = None
        if isinstance(data, Date):
            self.__data = data
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(prioridade, int):
            self.__prioridade = prioridade
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo

    @property
    def data(self) -> Date:
        return self.__data

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def tecnico(self) -> Tecnico:
        return self.__tecnico

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @property
    def tipo(self) -> TipoChamado:
        return self.__tipo
