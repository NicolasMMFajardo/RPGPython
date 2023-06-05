import numpy as np

Obstaculo = {0: 'caminho', 1: 'pedra', 2: 'Arbusto', 3: 'espinho'}


class Bloco:
    def __init__(self, obstaculo=0, conteminimigo=False, inimigo=None):
        self.Obstaculo = obstaculo
        self.ContemInimigo = conteminimigo
        self.inimigo = inimigo


class Mapa:
    def __init__(self):
        self.Matriz = np.full((16, 16), Bloco())


class Fase:
    def __init__(self, nome, mapa=Mapa()):
        self.Nome = nome
        self.MapaFase = mapa
