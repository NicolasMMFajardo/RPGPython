class Itens:
    def __init__(self, nome):
        self.Nome = nome


class Arma(Itens):
    def __init__(self, nome, danoMin=0):
        super().__init__(nome)
        self.DanoMin = danoMin
        self.DanoMax = danoMin * 3


class Armadura(Itens):
    def __init__(self, nome):
        super().__init__(nome)


class Bota(Itens):
    def __init__(self, nome):
        super().__init__(nome)
