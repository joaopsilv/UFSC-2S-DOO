

class Cargo():
    def __init__(self, titulo: str, salario: float) -> None:
        self.__titulo = None
        self.__salario = None
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(salario, float):
            self.__salario = salario

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        if isinstance(salario, float):
            self.__salario = salario
