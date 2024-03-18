from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = None
        self.__cliente = None
        self.__tipo = None
        self.__itens = []
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(tipo, TipoPedido):
            self.__tipo = tipo

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def tipo(self) -> TipoPedido:
        return self.__tipo

    @property
    def itens(self) -> list:
        return self.__itens

    @numero.setter
    def numero(self, numero):
        if isinstance(numero, int):
            self.__numero = int

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, TipoPedido):
            self.__tipo = tipo

    def inclui_item_pedido(self,
                           codigo: int,
                           descricao: str,
                           preco: float) -> ItemPedido:
        if self.busca_item_por_codigo(codigo) is None:
            item = ItemPedido(codigo, descricao, preco)
            self.__itens.append(item)
            return item
        return None

    def exclui_item_pedido(self, codigo: int) -> ItemPedido:
        item = self.busca_item_por_codigo(codigo)
        if item is not None:
            self.__itens.remove(item)
        return item

    def calcula_valor_pedido(self, distancia: float) -> float:
        valor = 0.0
        for item in self.__itens:
            valor += item.preco_unitario
        valor += self.__tipo.fator_distancia * distancia

        if isinstance(self.__cliente, ClienteFidelidade):
            valor -= valor * self.__cliente.desconto

        return valor

    def busca_item_por_codigo(self, codigo: int) -> ItemPedido:
        if self.__itens and isinstance(codigo, int):
            for item in self.__itens:
                if item.codigo == codigo:
                    return item
            return None
