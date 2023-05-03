import os
import time
import var
import classes

def start():
    os.system("clear")
    print("- Bem-Vindo(a) ao RPG -")
    time.sleep(3)
    os.system("clear")
    printNome = "Para começar sua aventura, insira o seu nome:"
    for i in printNome:
        print(i, end = '', flush = True)
        time.sleep(0.1)
    var.nome = input(" \n→ ")


    # tomada de decisão do nome
    os.system("clear")
    nomeConfirm = f"Você quer se chamar, {var.nome}?"
    for i in nomeConfirm:
        print(i, end = '', flush = True)
        time.sleep(0.1)
    time.sleep(1)
    print(" \n1. SIM\n2. NÃO")
    nameChoose = input("→ ")
    
    if nameChoose == "1" and nameChoose.isnumeric():
        classes.selecaoClasse()
    elif nameChoose == "2" and nameChoose.isnumeric():
        os.system("clear")
        novamente = "Vamos começar novamente."
        for i in novamente:
            print(i, end = '', flush=True)
            time.sleep(0.1)
        time.sleep(2)
        print("\n")
        start()
    else:
        os.system("clear")
        print("Escolha inválida.")
        time.sleep(2)
        start()