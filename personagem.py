import random
from item import Arma, Armadura, Bota


class Personagem:
    def __init__(self, vida, arma, nome):
        self.Vida = vida
        self.Arma = arma
        self.Nome = nome

    def morreu(self):
        if self.Vida <= 0:
            return True
        return False

    def ataque(self, alvo):
        alvo.Vida -= random.randint(self.Arma.DanoMin, self.Arma.DanoMax)
        return alvo


class Jogador(Personagem):
    def __init__(self, vida, arma, nome, pos_x=0, pos_y=0, armadura=None, bota=None):
        super().__init__(vida, arma, nome)
        self.PosX = pos_x
        self.PosY = pos_y
        self.Armadura = armadura
        self.Bota = bota

    def ataque(self, alvo):
        super().ataque(alvo)

    def morreu(self):
        super().morreu()


class Inimigo(Personagem):
    def __init__(self, vida, arma, nome):
        super().__init__(vida, arma, nome)

    def ataque(self, alvo):
        super().ataque(alvo)

    def morreu(self):
        super().morreu()
