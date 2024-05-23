class Jogo():
    def __init__(self):
        self.tabuleiro = [["","",""],
                          ["","",""],
                          ["","",""]]
    def vitoria(self):
        for check in "XO":
            for x in range(0,3):
                if self.tabuleiro[0][x] == check and self.tabuleiro[1][x] == check and self.tabuleiro[2][x] == check:
                    print("1!")
                elif self.tabuleiro[x][0] == check and self.tabuleiro[x][1] == check and self.tabuleiro[x][2] == check:
                    print("2!")
            if self.tabuleiro[2][0] == check and self.tabuleiro[1][1] == check and self.tabuleiro[0][2] == check:
                print("3!")
            elif self.tabuleiro[0][0] == check and self.tabuleiro[1][1] == check and self.tabuleiro[2][2] == check:
                print("4!")

