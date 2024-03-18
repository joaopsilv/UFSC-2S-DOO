from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        contador = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                contador += 1
        return contador

    def inclui_chamado(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado) -> Chamado:
        if (
                self.__buscar_chamado(data, cliente, tecnico, tipo) is None and
                isinstance(data, Date) and
                isinstance(cliente, Cliente) and
                isinstance(tecnico, Tecnico) and
                isinstance(titulo, str) and
                isinstance(descricao, str) and
                isinstance(prioridade, int) and
                isinstance(tipo, TipoChamado)):
            chamado = Chamado(
                data,
                cliente,
                tecnico,
                titulo,
                descricao,
                prioridade,
                tipo)
            self.__chamados.append(chamado)
            return chamado

    def inclui_tipochamado(
            self,
            codigo: int,
            nome: str,
            descricao: str) -> TipoChamado:
        if self.__buscar_tipo(codigo) is None:
            tipo = TipoChamado(codigo, descricao, nome)
            self.__tipos_chamados.append(tipo)
            return tipo

    @property
    def tipos_chamados(self) -> list:
        return self.__tipos_chamados

    def __buscar_chamado(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            tipo: TipoChamado) -> Chamado:
        for chamado in self.__chamados:
            if (
                    chamado.data == data and
                    chamado.cliente == cliente and
                    chamado.tecnico == tecnico and
                    chamado.tipo == tipo):
                return chamado

    def __buscar_tipo(self, codigo: int) -> TipoChamado:
        for tipo in self.__tipos_chamados:
            if tipo.codigo == codigo:
                return tipo
