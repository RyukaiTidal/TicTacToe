from classes import *

Turno = "X"
jogo = Jogo(Turno)

print("JOGO DA VÉIA")

while True:
    jogo.printarTabuleiro()
    print(f"É a vez do {jogo.turno}.")
    choice = int(input("Insira um numero de 1 a 9 \n-"))
    if 0 < choice < 10:
        jogo.jogada(choice)
    else:
        print("Número Incorreto.")
    if jogo.win == True:
        break
