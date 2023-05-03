import time
import os
import var
import frases
import lore

def selecaoClasse():
    os.system("clear")
    classeChoose = f"Olá {var.nome}, escolha sua classe:"
    #classeChoose = "Olá Erik, escolha sua classe com sabedoria:"
    for i in classeChoose:
        print(i, end='', flush=True)
        time.sleep(0.1)
    time.sleep(1)
    print("\n")
    choosing = True

    while choosing:
        print("1. Guerreiro\n2. Mago\n3. Ladino")
        var.classe = input("→ ")
       
        if var.classe == "1" and var.classe.isnumeric(): # PRINT DA CLASSE GUEREIRO
            var.classe = 0
            os.system("clear")
            print("→ Classe Guerreiro")
            for i in frases.fraseGuerreiro[0]:
                print(i, end='', flush=True)
                time.sleep(0.03)
            print("\n")
            for i in frases.atributosGuerreiro[0]:
                print(i, end='', flush=True)
                time.sleep(0.05)
            time.sleep(2)
            print("\n")
            print("Confirma a seleção desta classe?")
            print("1. SIM\n2. NÃO")
            guerreiroChoose = input("→ ")
            if guerreiroChoose == "1" and guerreiroChoose.isnumeric():
                lore.start()
                choosing = False
            elif guerreiroChoose == "2" and guerreiroChoose.isnumeric():
                pass
            else:
                invalidaChoose = "Escolha inválida."
                for i in invalidaChoose:
                    print(i, end='', flush=True)
                    time.sleep(0.1)
                time.sleep(1)
                os.system("clear")

        elif var.classe == "2" and var.classe.isnumeric(): # PRINT DA CLASSE MAGO
            var.classe = 1
            os.system("clear")
            print("→ Classe Mago")
            for i in frases.fraseMago[0]:
                print(i, end='', flush=True)
                time.sleep(0.03)
            print("\n")
            for i in frases.atributosMago[0]:
                print(i, end='', flush=True)
                time.sleep(0.05)
            time.sleep(2)
            print("\n")
            print("Confirma a seleção desta classe?")
            print("1. SIM\n2. NÃO")
            magoChoose = input("→ ")
            if magoChoose == "1" and magoChoose.isnumeric():
                lore.start()
                choosing = False
            elif magoChoose == "2" and magoChoose.isnumeric():
                pass
            else:
                invalidaChoose = "Escolha inválida."
                for i in invalidaChoose:
                    print(i, end='', flush=True)
                    time.sleep(0.1)
                time.sleep(1)
                os.system("clear")

        elif var.classe == "3" and var.classe.isnumeric(): # PRINT DA CLASSE LADINO
            var.classe = 2
            os.system("clear")
            print("→ Classe Ladino")
            for i in frases.fraseLadino[0]:
                print(i, end='', flush=True)
                time.sleep(0.03)
            print("\n")
            for i in frases.atributosLadino[0]:
                print(i, end='', flush=True)
                time.sleep(0.05)
            time.sleep(2)
            print("\n")
            print("Confirma a seleção desta classe?")
            print("1. SIM\n2. NÃO")
            ladinoChoose = input("→ ")
            if ladinoChoose == "1" and ladinoChoose.isnumeric():
                lore.start()
                choosing = False
            elif ladinoChoose == "2" and ladinoChoose.isnumeric():
                pass
            else:
                invalidaChoose = "Escolha inválida."
                for i in invalidaChoose:
                    print(i, end='', flush=True)
                    time.sleep(0.1)
                time.sleep(1)
                os.system("clear")
        
        else:
            invalidaChoose = "Escolha inválida."
            for i in invalidaChoose:
                print(i, end='', flush=True)
                time.sleep(0.1)
            time.sleep(1)
            os.system("clear")
        
        os.system("clear")