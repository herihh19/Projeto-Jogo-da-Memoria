#TRABALHO DE LAB2#

from time import sleep
#sleep serve pra dar um delay no tempo
from random import randint
# random pra gerar numeros aleatórios no jogo

def limpar():
    print("\n" * 50)
    #função de limpar que imprime 50 linhas em branco, para não ver a tela do jogo

def verifica(m, mp):
    cont = 0
    for i in range(0, 4):
        for c in range(0, 4):
            if m[i][c] == mp:
                cont += 1
    if cont > 2:
        return True
#verifica se o valor "mp" ocorre mais de 2x na matriz "m" e retorna True se for o caso.

def mostraMatriz(i1, c1, i2, c2, m):
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matriz[i1 - 1][c1 - 1] = m[i1 - 1][c1 - 1]
    matriz[i2 - 1][c2 - 1] = m[i2 - 1][c2 - 1]
#

    for i in range(0, 4):
        for c in range(0, 4):
            print(matriz[i][c], end="")
        print("\n")

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#matriz vazia que será preenchida com números aleatórios
print("\n\033[1;32m=- JOGO DA MEMÓRIA -=" * 15 + "\033[m")
print("\n\033[1;33mPares certos: 1 Ponto")
print("Pares errados: -1 ponto\033[m")
print("\n\033[1;31mINSTRUÇÕES\n\n"
      "O TABULEIRO POSSUI 4 LINHAS E 4 COLUNAS\n"
      "PARA CONTINUAR A JOGAR CLIQUE NA TECLA S (AO FIM DE CADA JOGADA SERÁ PERGUNTADO)\033[m")

a = str(input("\n\033[1;32mDIGITE C PARA COMEÇAR: \033[m"))
if a == "c":
    print("\n\033[1;34mO JOGO DA MEMÓRIA COMEÇA EM 10 SEGUNDOS\n")
    #contagem para o jogo começar:
    for cont in range(10, 0, -1):
        print(cont)
        sleep(1)
    

    print("\n\033[m")
    print("VOCÊ TEM 8 SEGUNDOS PARA MEMORIZAR\n")
    
    for i in range(0, 4):
        for c in range(0, 4):
            matriz[i][c] = randint(1, 8)
            while verifica(matriz, matriz[i][c]):
                matriz[i][c] = randint(1, 8)
            print(matriz[i][c], end="")
        print("\n")
    sleep(8)
    limpar()
    #imprime a matriz inicial do jogo, que tem os números aleatórios de 1 a 8, 
    # e o jogador tem 8 segundos para memorizar. A função "verifica" é usada 
    #para que não tenha mais de 2 números idênticos na matriz.Após 8s , a função limpar limpa a tela.

    r = "s" #se o jogador colocar "s" ele continua o jogo
    pt = 0

    while r == "s":
        i1 = int(input("INFORME A PRIMEIRA JOGADA: (LINHA, COLUNA)\n"))
        c1 = int(input())
        i2 = int(input("INFORME A SEGUNDA JOGADA: (LINHA, COLUNA)\n"))
        c2 = int(input())

        print("\n" * 2)
        print(matriz[i1 - 1][c1 - 1])
        print(matriz[i2 - 1][c2 - 1])
        print("\n" * 2)
        mostraMatriz(i1, c1, i2, c2, matriz)
        if matriz[i1 - 1][c1 - 1] == matriz[i2 - 1][c2 - 1]:
            print("PARABÉNS VOCÊ ACERTOU :D!!")
            pt += 1
        else:
            pt -= 1
            print("VOCÊ ERROU :C")
        r = str(input("DESEJA CONTINUAR: [s] ou [n] ?"))
        #r=s
    
    print(f"PONTUAÇÃO - {pt} ")
    #pontuação final do jogador.
