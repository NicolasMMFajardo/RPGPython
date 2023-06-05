from personagem import Personagem, Jogador, Inimigo
from item import Arma, Armadura, Bota
from fase import Bloco, Mapa, Fase
from jogar import batalha

graveto = Arma("graveto", 1)
goblin = Inimigo(10, graveto, "Goberto")
machado = Arma("machado", 10)
nicolas = Jogador(100, machado, "Nicolas")
CampoDasFeras = Fase("Campo das Feras")

batalha(nicolas, goblin)
