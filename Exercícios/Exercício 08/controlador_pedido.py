from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    def busca_pedido_por_numero(self, numero: int) -> Pedido:
        if self.__pedidos and isinstance(numero, int):
            for pedido in self.__pedidos:
                if pedido.numero == numero:
                    return pedido
            return None

    def incluir_pedido(self, pedido: Pedido) -> Pedido:
        if isinstance(pedido, Pedido):
            if self.busca_pedido_por_numero(pedido.numero) is not None:
                raise PedidoDuplicadoException
            self.__pedidos.append(pedido)
        return pedido

    def excluir_pedido(self, numero: int) -> Pedido:
        pedido = self.busca_pedido_por_numero(numero)
        if pedido is not None:
            self.__pedidos.remove(pedido)
        return pedido

    def calcular_faturamento_pedidos(self,
                                     distancia: float,
                                     cpf: str) -> float:
        faturamento = 0.0
        for pedido in self.__pedidos:
            if pedido.cliente.cpf == cpf:
                faturamento += pedido.calcula_valor_pedido(distancia)
        return faturamento
