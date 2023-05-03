import play.inventario
import var
import os
import time
import play.loja
import random

# var.nome = "Erik"
# var.classeipt = ["Guerreiro", "Mago", "Ladino"]
# var.classe = 0 #random.randint(0, 2)

def startGame():
    playing = True
    while playing:
        os.system("clear")
        print(f"    O          Nome: {var.nome}, O {var.classeipt[var.classe]}")
        print(f"   /|\         Vida: {var.vida}%")
        print(f"   / \         Ouro: {var.ouro}")
        print(f"               Nível: {var.nivel}")
        print("────────────────────────────────────────────────────────────")
        print("       1. Lutar     2. Inventário     3. Loja")
        print("────────────────────────────────────────────────────────────")
        menuChoose = input("→ ")

        if menuChoose == "1" and menuChoose.isnumeric():
            print("LUTAR")
            time.sleep(2)
        
        elif menuChoose == "2" and menuChoose.isnumeric():
            play.inventario.inv()

        elif menuChoose == "3" and menuChoose.isnumeric():
            play.loja.loja()