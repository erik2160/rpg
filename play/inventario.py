import var
import play.playing
import os
import ascii.gweapons

global c
invSet = []
global iv
iv = 1, 2, 3, 4
def inv():
    global iv
    global c
    os.system("clear")

    if var.classe == 0:
        invSet = var.inventarioG
        c = 0
        x = 0
        for i in invSet:
            c += 1
            print(f"{c}. {invSet[x]}")
            x += 1

    if var.classe == 1:
        invSet = var.inventarioM
        c = 0
        x = 0
        for i in invSet:
            c += 1
            print(f"{c}. {invSet[x]}")
            x += 1

    if var.classe == 2:
        invSet = var.inventarioL
        c = 0
        x = 0
        for i in invSet:
            c += 1
            print(f"{c}. {invSet[x]}")
            x += 1

    print("────────────────────────────────────────────────────────────")
    print(" Digite o ID de um Item para selecionar ou Enter para voltar")
    print("────────────────────────────────────────────────────────────")
    invSelect = input("→ ")

    if invSelect == "":
        play.playing.startGame()       

    if invSelect == "1" and invSelect.isdigit() and (c == 1 or c == 2 or c == 3 or c == 4):
        os.system("clear")
        # SE A CLASSE FOR GUERREIRO, VAI PRINTAR OS MACHADOS
        if var.classe == 0:
            print(ascii.gweapons.firstAxe[0])
            print(ascii.gweapons.fAxeStats[0])
            print("────────────────────────────────────────────────────────────")
            print("              Pressione Enter para voltar")
            print("────────────────────────────────────────────────────────────")
            invSelect = input("→ ")
            inv()

        # SE A CLASSE FOR MAGO, VAI PRINTAR OS ITENS
        if var.classe == 1:
            pass

        # SE A CLASSE FOR LADINO VAI PRINTAR OS ITENS
        if var.classe == 2:
            pass

    elif invSelect == "2" and invSelect.isdigit() and (c == 2 or c == 3 or c == 4):
        
        # SE A CLASSE FOR GUERREIRO, VAI PRINTAR OS MACHADOS 2
        if var.classe == 0:
            os.system("clear")
            print(ascii.gweapons.secondAxe[0])
            print(ascii.gweapons.sAxeStats[0])
            print("────────────────────────────────────────────────────────────")
            print("              Pressione Enter para voltar")
            print("────────────────────────────────────────────────────────────")
            invSelect = input("→ ")
            inv()
        
        # SE A CLASSE FOR MAGO, VAI PRINTAR OS ITENS 2
        if var.classe == 1:
            pass

        # SE A CLASSE FOR LADINO VAI PRINTAR OS ITENS 2
        if var.classe == 2:
            pass

    elif invSelect == "3" and invSelect.isdigit() and (c == 3 or c == 4):
        
        # SE A CLASSE FOR GUERREIRO, VAI PRINTAR OS MACHADOS 2
        if var.classe == 0:
            os.system("clear")
            print(ascii.gweapons.thirdAxe[0])
            print(ascii.gweapons.tAxeStats[0])
            print("────────────────────────────────────────────────────────────")
            print("              Pressione Enter para voltar")
            print("────────────────────────────────────────────────────────────")
            invSelect = input("→ ")
            inv()
        
        # SE A CLASSE FOR MAGO, VAI PRINTAR OS ITENS 2
        if var.classe == 1:
            pass

        # SE A CLASSE FOR LADINO VAI PRINTAR OS ITENS 2
        if var.classe == 2:
            pass

    elif invSelect == "4" and invSelect.isdigit() and (c == 4):
        
        # SE A CLASSE FOR GUERREIRO, VAI PRINTAR OS MACHADOS 2
        if var.classe == 0:
            os.system("clear")
            print(ascii.gweapons.fourAxe[0])
            print(ascii.gweapons.frAxeStats[0])
            print("────────────────────────────────────────────────────────────")
            print("              Pressione Enter para voltar")
            print("────────────────────────────────────────────────────────────")
            invSelect = input("→ ")
            inv()
        
        # SE A CLASSE FOR MAGO, VAI PRINTAR OS ITENS 2
        if var.classe == 1:
            pass

        # SE A CLASSE FOR LADINO VAI PRINTAR OS ITENS 2
        if var.classe == 2:
            pass
        
    else:
        inv()