from cliente import Cliente


class Produto:
    def __init__(self, codigo: int, descricao: str, categoria: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(categoria, str):
            self.__categoria_produto = categoria
        self.__quantidade = None
        self.__preco_unitario = None
        self.__cliente = None

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def categoria_produto(self) -> str:
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto: str):
        if isinstance(categoria_produto, str):
            self.__categoria_produto = categoria_produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade

    @property
    def preco_unitario(self) -> float:
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario: float):
        if isinstance(preco_unitario, float):
            self.__preco_unitario = preco_unitario

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def preco_total(self):
        return self.__quantidade * self.__preco_unitario
