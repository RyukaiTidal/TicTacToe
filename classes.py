class Jogo():
    def __init__(self, turno):
        self.tabuleiro = [["7", "8", "9"],
                          ["4", "5", "6"],
                          ["1", "2", "3"]]
        self.turno = turno
        self.win = False
        self.contador = 1

    def vitoria(self):
        for check in "XO":
            for x in range(0, 3):
                if self.tabuleiro[0][x] == check and self.tabuleiro[1][x] == check and self.tabuleiro[2][x] == check:
                    self.tabuleiro[0][x] = "|"
                    self.tabuleiro[1][x] = "|"
                    self.tabuleiro[2][x] = "|"
                    self.printarTabuleiro()
                    print(f"Um Jogador fez Linha na Vertical.\nVitória do {self.turno}!")
                    self.win = True
                elif self.tabuleiro[x][0] == check and self.tabuleiro[x][1] == check and self.tabuleiro[x][2] == check:
                    self.tabuleiro[x][0] = "-"
                    self.tabuleiro[x][1] = "-"
                    self.tabuleiro[x][2] = "-"
                    self.printarTabuleiro()
                    print(f"Um jogador fez Linha na Horizontal. \n Vitória do {self.turno}!")
                    self.win = True
            if self.tabuleiro[2][0] == check and self.tabuleiro[1][1] == check and self.tabuleiro[0][2] == check:
                self.tabuleiro[2][0] = "/"
                self.tabuleiro[1][1] = "/"
                self.tabuleiro[0][2] = "/"
                self.printarTabuleiro()
                print(f"Um jogador fez Linha na Diagonal Direita. \n Vitória do {self.turno}!")
                self.win = True
            elif self.tabuleiro[0][0] == check and self.tabuleiro[1][1] == check and self.tabuleiro[2][2] == check:
                self.tabuleiro[0][0] = "\\"
                self.tabuleiro[1][1] = "\\"
                self.tabuleiro[2][2] = "\\"
                self.printarTabuleiro()
                print(f"Um jogador fez Linha na Diagonal Esquerda. \n Vitória do {self.turno}!")
                self.win = True
            if self.win == False and self.contador > 9:
                self.printarTabuleiro()
                print("Ninguém conseguiu fazer Linha. Deu Velha!")
                self.win = True

    def printarTabuleiro(self):
        print(f" {self.tabuleiro[0][0]} | {self.tabuleiro[0][1]} | {self.tabuleiro[0][2]}\n"
              f"---|---|---\n"
              f" {self.tabuleiro[1][0]} | {self.tabuleiro[1][1]} | {self.tabuleiro[1][2]}\n"
              f"---|---|---\n"
              f" {self.tabuleiro[2][0]} | {self.tabuleiro[2][1]} | {self.tabuleiro[2][2]}\n")

    def jogada(self, play):
        c = 2
        l = 0
        for num in range(1, 10):
            if num == play:
                if self.tabuleiro[c][l] in "XO":
                    print("Casa já Preenchida. Tente Novamente.")
                else:
                    self.tabuleiro[c][l] = self.turno
                    Jogo.vitoria(self)
                    if self.turno == "X":
                        self.turno = "O"
                    elif self.turno == "O":
                        self.turno = "X"
                    self.contador += 1
                continue
            l += 1
            if l > 2:
                l = 0
                c -= 1
