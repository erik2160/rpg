import os
import var
import play.playing
import ascii.gweapons

def loja():
    os.system("clear")
    print("1. Armas")
    print("2. Poções")
    print("3. Especiais")
    print("────────────────────────────────────────────────────────────────")
    print(" Digite o ID da Categoria para selecionar ou Enter para voltar")
    print("────────────────────────────────────────────────────────────────")
    lojaSelect = input("→ ")

    if lojaSelect == " ":
        play.playing.startGame()

    if lojaSelect == "1" and lojaSelect.isdigit():
        os.system("clear")
        # SE A CLASSE FOR GUERREIRO, VAI PRINTAR OS ITENS DO GUERREIRO

        if var.classe == 0:
            print("1. Machado Médio")
            print("2. Machado Forte")
            print("3. Machado Celeste")
            print("────────────────────────────────────────────────────────────────")
            print("      Digite o ID para selecionar ou Enter para voltar")
            print("────────────────────────────────────────────────────────────────")
            machadoSelect = input("→ ")

            if machadoSelect == " ": # APERTOU ENTER, VOLTA
                loja()
                
            # COMEÇO COMPRA MACHADO MEDIO
            if machadoSelect == "1" and machadoSelect.isdigit(): # SELEÇÃO DO MACHADO MEDIO E PRINTS
                if "Machado Médio" in var.inventarioG:
                    os.system("clear")
                    print("────────────────────────────────────────────────────────────────")
                    print("     Você já possui esse item, pressione Enter para voltar")
                    print("────────────────────────────────────────────────────────────────")
                    input("")
                    loja()
                else:
                    os.system("clear")
                    print(ascii.gweapons.secondAxe[0])
                    print(f"{ascii.gweapons.sAxeStats[0]}\n• Preço: {ascii.gweapons.sAxePrice} Ouro(s), você tem {var.ouro} Ouros")
                    print("────────────────────────────────────────────────────────────────")
                    print("           Digite 1 para Comprar ou Enter para voltar")
                    print("────────────────────────────────────────────────────────────────")
                    machadoBuy = input("→ ")

                    if machadoBuy == " ":
                        loja()

                    # COMPRA DO MACHADO MÉDIO
                    if machadoBuy == "1" and machadoBuy.isdigit():
                        if var.ouro >= ascii.gweapons.sAxePrice: # verif do seu ouro
                            var.inventarioG.append("Machado Médio") # adiciona o item no seu inventario
                            var.ouro -= ascii.gweapons.sAxePrice # diminui o ouro da sua conta
                        else:
                            print("sem ouro, irmão")
                            input("")
                            loja()
            # FIM COMPRA MACHADO MEDIO

            # COMEÇO COMPRA MACHADO FORTE
            if machadoSelect == "2" and machadoSelect.isdigit(): # SELEÇÃO DO MACHADO FORTE E PRINTS
                if "Machado Forte" in var.inventarioG:
                    os.system("clear")
                    print("────────────────────────────────────────────────────────────────")
                    print("     Você já possui esse item, pressione Enter para voltar")
                    print("────────────────────────────────────────────────────────────────")
                    input("")
                    loja()
                else:
                    os.system("clear")
                    print(ascii.gweapons.thirdAxe[0])
                    print(f"{ascii.gweapons.tAxeStats[0]}\n• Preço: {ascii.gweapons.tAxePrice} Ouro(s), você tem {var.ouro} Ouros")
                    print("────────────────────────────────────────────────────────────────")
                    print("           Digite 1 para Comprar ou Enter para voltar")
                    print("────────────────────────────────────────────────────────────────")
                    machadoBuy = input("→ ")

                    if machadoBuy == " ":
                        loja()

                    # COMPRA DO MACHADO FORTE
                    if machadoBuy == "1" and machadoBuy.isdigit():
                        if var.ouro >= ascii.gweapons.tAxePrice: # verif do seu ouro
                            var.inventarioG.append("Machado Forte") # adiciona o item no seu inventario
                            var.ouro -= ascii.gweapons.tAxePrice # diminui o ouro da sua conta
                        else:
                            print("sem ouro, irmão")
                            input("")
                            loja()
            # FIM COMPRA MACHADO FORTE

            # COMEÇO COMPRA MACHADO CELESTIAL
            if machadoSelect == "3" and machadoSelect.isdigit(): # SELEÇÃO DO MACHADO CELESTIAL E PRINTS
                if "Machado Celestial" in var.inventarioG:
                    os.system("clear")
                    print("────────────────────────────────────────────────────────────────")
                    print("     Você já possui esse item, pressione Enter para voltar")
                    print("────────────────────────────────────────────────────────────────")
                    input("")
                    loja()
                else:
                    os.system("clear")
                    print(ascii.gweapons.fourAxe[0])
                    print(f"{ascii.gweapons.frAxeStats[0]}\n• Preço: {ascii.gweapons.frAxePrice} Ouro(s), você tem {var.ouro} Ouros")
                    print("────────────────────────────────────────────────────────────────")
                    print("           Digite 1 para Comprar ou Enter para voltar")
                    print("────────────────────────────────────────────────────────────────")
                    machadoBuy = input("→ ")

                    if machadoBuy == " ":
                        loja()

                    # COMPRA DO MACHADO CELESTIAL
                    if machadoBuy == "1" and machadoBuy.isdigit():
                        if var.ouro >= ascii.gweapons.frAxePrice: # verif do seu ouro
                            var.inventarioG.append("Machado Celestial") # adiciona o item no seu inventario
                            var.ouro -= ascii.gweapons.frAxePrice # diminui o ouro da sua conta
                        else:
                            print("sem ouro, irmão")
                            input("")
                            loja()
            # FIM COMPRA MACHADO CELESTIAL


        if var.classe == 1: # SE A CLASSE FOR MAGO
            pass

        if var.classe == 2: # SE A CLASSE FOR LADINO
            pass