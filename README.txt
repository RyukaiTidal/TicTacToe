Código de verificação de vitória

Tabuleiro do Jogo:

 0,0 | 0,1 | 0,2
-----|-----|-----
 1,0 | 1,1 | 1,2
-----|-----|-----
 2,0 | 2,1 | 2,2

Ex: Tabuleiro[0][1]

 0,0 |(0,1)| 0,2
-----|-----|-----
 1,0 | 1,1 | 1,2
-----|-----|-----
 2,0 | 2,1 | 2,2

onde [x] é a linha e [y] é a coluna.

"for check in "XO":"

# Verifica para os dois jogadores, primeiro o X, depois o O

"for x in range(0,3):"

# Verifica 3 vezes, onde o parâmetro X vai de 0 até 2 (0,1,2)

"if self.tabuleiro[0][x] == check and self.tabuleiro[1][x] == check and self.tabuleiro[2][x] == check"

# Ele Verifica se ocorreu uma linha Vertical em: [0,0 ; 1,0 ; 2,0] , [1,0 ; 1,1 ; 1,2] e [2,0 ; 2,1 ; 2,2].

Ordem de Verificação

 0|0 | 0|1 | 0|2
--|--|--|--|--|--
 1|0 | 1|1 | 1|2
--|--|--|--|--|--
 2|0 | 2|1 | 2|2


"elif self.tabuleiro[x][0] == check and self.tabuleiro[x][1] == check and self.tabuleiro[x][2] == check:"

# Agora ele verifica se ocorreu uma linha horizontal em [0,0 ; 0,1 ; 0,2] , [1,0 ;1,1; 1,2] e [2,0 ; 2,1 ; 2,2]

Ordem de Verificação

-0-0-|-0-1-|-0-2-
-----|-----|-----
-1-0-|-1-1-|-1-2-
-----|-----|-----
-2-0-|-2-1-|-2-2-

 

"if self.tabuleiro[2][0] == check and self.tabuleiro[1][1] == check and self.tabuleiro[0][2] == check:"

# Verifica a Primeira Diagonal do  Jogo:


 0,0 | 0,1 | /
-----|-----|-----
 1,0 |  /  | 1,2
-----|-----|-----
  /  | 2,1 | 2,2


"elif self.tabuleiro[0][0] == check and self.tabuleiro[1][1] == check and self.tabuleiro[2][2] == check:"

# Agora ele Verifica a ultima diagonal.

   \ | 0,1 | 0,2
-----|-----|-----
 1,0 |  \  | 1,2
-----|-----|-----
 2,0 | 2,1 |  \


