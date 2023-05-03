import var
import time
import os
import ascii.player
import play.playing
import others

def start():
    os.system("clear")

    print("Carregando", end='')
    pontos = "...."
    for i in pontos:
        print(i, end='', flush=True)
        time.sleep(0.9)

    os.system("clear")
    lore = f"Há muitos anos, um homem chamado {others.var.nome} estava viajando pelo mundo em busca de aventuras. Em uma de suas viagens, ele chegou a um antigo templo abandonado, cujas paredes estavam cobertas de musgos e cujos corredores estavam repletos de símbolos estranhos e indecifráveis."
    for i in lore:
        print(i, end='', flush=True)
        time.sleep(0.02)
    print(" \n")
    time.sleep(2)
    
    lore2 = f"{others.var.nome} estava tão fascinado com o lugar que decidiu explorá-lo sozinho. No entanto, enquanto caminhava pelos corredores escuros, ele não percebeu uma vala profunda à sua frente e acabou caindo nela."
    for i in lore2:
        print(i, end='', flush=True)
        time.sleep(0.02)
    print(" \n")
    time.sleep(2)

    lore3 = f"Quando acordou, {others.var.nome} percebeu que estava em uma caverna escura e úmida, cercado por monstros estranhos que nunca havia visto antes. Com seu instinto de sobrevivência aguçado, ele percebeu que precisava lutar contra os monstros para conseguir sair do local."
    for i in lore3:
        print(i, end='', flush=True)
        time.sleep(0.02)
    print(" \n")
    time.sleep(2)

    lore4 = f"{others.var.nome} se escondeu em um local que parecia seguro, e começou a pensar em uma forma de escapar."
    for i in lore4:
        print(i, end='', flush=True)
        time.sleep(0.02)
    print(" \n")
    time.sleep(2)

    lore5 = f"E assim, sua aventura começa..."
    for i in lore5:
        print(i, end='', flush=True)
        time.sleep(0.1)
    print(" \n")
    time.sleep(2)

    enter = "Pressione Enter para continuar..."
    for i in enter:
        print(i, end='', flush=True)
        time.sleep(0.1)
    input("")

    os.system("clear")    
    print(ascii.player.playerDraw[0])
    time.sleep(2)
    
    voce = f"Este é você, {others.var.nome}.\nNeste mundo, você precisa lutar contra monstros para sobreviver.\nHá um total de 10 níveis e 10 bosses, você precisa eliminar todos para vencer.\nCompre e melhore seus equipamentos na loja, compre itens para lhe proteger ou aumentar seu HP.\nQue a sorte esteja com você.."
    for i in voce:
        print(i, end='', flush=True)
        time.sleep(0.09)

    print(" \n")
    for i in enter:
        print(i, end='', flush=True)
        time.sleep(0.1)
    input("")
    play.playing.startGame()