def batalha(player, inimigo):
    morteInimigo = False
    while morteInimigo == False:

        player = player.ataque(inimigo)
        print(inimigo.Nome + " atacou " + player.Nome + " que ficou com " + str(player.Vida) + " de vida.\n")
        inimigo = player.ataque(player)
        print(player.Nome + " atacou " + inimigo.Nome + " que ficou com " + str(inimigo.Vida) + " de vida.\n")

        if player.morreu():
            print(player.Nome + " morreu!\n")
            input()
            return player

        if inimigo.morreu():
            print(inimigo.Nome + " foi morto!\n\n")
            morteInimigo = True

    return player
