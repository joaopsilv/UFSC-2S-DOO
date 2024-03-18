from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(
            self, codigo: int, titulo: str, ano: int, editora: Editora,
            autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(ano, int):
            self.__ano = ano
        if isinstance(editora, Editora):
            self.__editora = editora
        if isinstance(autor, Autor):
            self.__autores = [autor]
        if isinstance(numero_capitulo, int) and isinstance(titulo_capitulo, str):
            self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        if isinstance(numero, int) and isinstance(titulo, str):
            novo_capitulo = Capitulo(numero, titulo)
            if not any(capitulo.titulo == titulo for capitulo in self.__capitulos):
                self.__capitulos.append(novo_capitulo)

    def excluir_capitulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
