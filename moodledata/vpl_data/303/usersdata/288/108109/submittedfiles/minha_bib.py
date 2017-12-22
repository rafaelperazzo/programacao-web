# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

import random 
def solicitaSimboloDoHumano():
    simbolo=str(input("Escolha um simbolo para jogar (X ou O): "))
    while (simbolo)!= "X" and (simbolo)!="O" and (simbolo)!="x" and (simbolo)!="o":
        print ("Simbolo invalido!")
        simbolo=str(input("Escolha um simbolo CORRETO para jogar! (X ou O): "))
    if simbolo=="X" or (simbolo)=="x":
        return ['X','O']
    else:
        return ['O','X']

def sorteioPrimeiraJogada():
    if random.randint(1,2)==1:
        return "Computador"
    else:
        return "Voce"

#movimento no jogo:

def jogadaHumana(tabuleiro):
    movimento = 0
    while movimento not in '1 2 3 4 5 6 7 8 9' or not vazio(tabuleiro, int(movimento)):
        movimento=input("\nQual a sua jogada?")
        if movimento == "0 0":
            movimento= "7"
        elif movimento== "0 1":
            movimento="8"
        elif movimento== "0 2":
            movimento="9"
        elif movimento== "1 0":
            movimento="4"
        elif movimento== "1 1":
            movimento="5"
        elif movimento=="1 2":
            movimento="6"
        elif movimento=="2 0":
            movimento="1"
        elif movimento=="2 1":
            movimento="2"
        elif movimento=="2 2":
            movimento="3"
            
    return int(movimento)
    
    
def jogada(tabuleiro, simbolo, movimento):
    tabuleiro[movimento] = simbolo
    

def verificaVencedor(tabuleiro, simbolo):
    return ((tabuleiro[1] == simbolo and tabuleiro[2] == simbolo and tabuleiro[3] == simbolo) or   #linhas vencedoras
 (tabuleiro[4] == simbolo and tabuleiro[5] == simbolo and tabuleiro[6] == simbolo) or     
 (tabuleiro[7] == simbolo and tabuleiro[8] == simbolo and tabuleiro[9] == simbolo) or
 (tabuleiro[7] == simbolo and tabuleiro[4] == simbolo and tabuleiro[1] == simbolo) or              #colunas vencedoras
 (tabuleiro[8] == simbolo and tabuleiro[5] == simbolo and tabuleiro[2] == simbolo) or     
 (tabuleiro[9] == simbolo and tabuleiro[6] == simbolo and tabuleiro[3] == simbolo) or  
 (tabuleiro[7] == simbolo and tabuleiro[5] == simbolo and tabuleiro[3] == simbolo) or              #diagonais vencedoras
 (tabuleiro[9] == simbolo and tabuleiro[5] == simbolo and tabuleiro[1] == simbolo))
    

def completo(tabuleiro):
    for i in range(1, 10):
        if vazio(tabuleiro, i):
            return False
    return True

def vazio(tabuleiro, movimento):
    if tabuleiro[movimento] == ' ':
        return True
    

#comportamento das funções para dadas jogadas:

def jogadaComputador(tabuleiro, simboloComputador):
    if simboloComputador == "X":
        simboloVoce = "O"
    else:
        simboloVoce = "X"
    for i in range(1,10):
        mostra = mostraTabuleiro(tabuleiro)
        if vazio(mostra, i):
            jogada(mostra, simboloComputador, i)
            if verificaVencedor(mostra, simboloComputador):
                return i

    for i in range(1, 10):
        mostra = mostraTabuleiro(tabuleiro)
        if vazio(mostra, i):
            jogada(mostra, simboloVoce, i)
            if verificaVencedor(mostra, simboloVoce):
                return i

    movimento = movAleatoria(tabuleiro, [1, 3, 7, 9])
    if movimento != None:
        return movimento

    if vazio(tabuleiro, 5):
        return 5

    return movAleatoria(tabuleiro, [2, 4, 6, 8])



def mostraTabuleiro(tabuleiro):
    dupeTabuleiro = []

    for i in tabuleiro:
        dupeTabuleiro.append(i)

    return dupeTabuleiro


 


def desenhaTabuleiro(tabuleiro):
    print(" " + tabuleiro[7] + " | " + tabuleiro[8] + " | " + tabuleiro[9])
    print ("---+---+---")
    print(" " + tabuleiro[4] + " | " + tabuleiro[5] + " | " + tabuleiro[6])
    print ("---+---+---")
    print(" " + tabuleiro[1] + " | " + tabuleiro[2] + " | " + tabuleiro[3])



def jogarNovamente():
    jogar=str(input("Você deseja jogar novamente? "))
    if jogar==("SIM") or jogar==("sim"):
        return True
    elif jogar==("NAO") or jogar==("nao"):
        return False




def movAleatoria(tabuleiro, movimentosList):
    movPossiveis = []
    for i in movimentosList:
        if vazio(tabuleiro, i):
            movPossiveis.append(i)

    if len(movPossiveis) != 0:
        return random.choice(movPossiveis)
    else:
        return None


"""


#JJ


velha=  Jogadas      Posições jogáveis
   |   |           7 | 8 | 9
---+---+---       ---+---+---
   |   |           4 | 5 | 6
---+---+---       ---+---+---
   |   |           1 | 2 | 3

# Listagem de posicoes (horizontal e vertical) para as posicoes do jogo.
# Numeração das posicoes ira facilitar o entendimento para jogabilidade.


posicoes = [
  None,  # Indice
  (5, 1), # 1
  (5, 5), # 2
  (5, 9), # 3
  (3, 1), # 4
  (3, 5), # 5
  (3, 9), # 6
  (1, 1), # 7
  (1, 5), # 8
  (1, 9), # 9
]

# Descrição das posicoes que ganham o jogo fazendo uma linha, um coluna, linha ou diagonal == win
# Os números representam as posicoes ganhadoras
win = [
      [ 1, 2, 3], #linha
      [ 4, 5, 6],
      [ 7, 8, 9],
      [ 7, 4, 1], #coluna
      [ 8, 5, 2],
      [ 9, 6, 3],
      [ 7, 5, 3], #diag
      [ 1, 5, 9]
    ]

# Tabuleiro é construido usndo string e gera lista

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))

jogador = "X" # Começa jogando com X
jogando = True
jogada = 0 # Contador de jogadas
while True:
    for t in tabuleiro:  # Mostra o tabuleiro
        print("".join(t))
    if not jogando: # Termina após mostrar o último tabuleiro
        break
    if jogada == 9: # Se 9 jogadas, todas as posicoes já foram preenchidas
        print("Deu velha! Ninguém ganhou.")
        break
    jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" % jogador))
    if jogada<1 or jogada>9:
        print("Posição inválida")
        continue
# Verifica posição livre
    if tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] != " ":
        print("Posição ja utilizada ocupada.")
        continue
# Marca a jogada p/ o jogador
tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] = jogador
# Verfica se ganhou
for p in win:
    for x in p:
        if tabuleiro[posicoes[x][0]][posicoes[x][1]] != jogador:
            break
    else: # Se o for terminar sem break, todas as posicoes de p pertencem ao mesmo jogador
        print("O jogador %s ganhou (%s): "%(jogador, p))
        jogando = False
        break
jogador = "X" if jogador == "O" else "O" # Alterna os jogador
jogada +=1 # Contador de jogadas

def maximo (a,b):
    if a>b:
        return a
    else:
        return b
    
lista1.append(input('Digite um valor: '))
lista1[len(lista1)]
len(lista1)
lista1[len(lista1)-1]
lista1[len(lista1)+1]


def par(n):
    if (n%2)==0:
        return True
    else:
        return False

def f1(x,y):
    return ((x*y)/(x-y))

def avaliar(z):
    resultado=z
    if z<0:
        resultado *= (-1)
    return resultado

def multiplicacao(x,y):
    return (x*y)

def funcao(a,b,c):
    if (a+b)==c:
        return True
    else:
        return False

def simbolo ():
    simbolo=str(input("Escolha um simbolo [X ou O]: "))
    while (simbolo!='X' and simbolo!='O'):
            print ("SIMBOLO INVALIDO!")
            simbolo=str(input("Escolha um simbolo [X ou O]: "))
    print ("pronto")
    

def fatorial(n):
    f=1
    for i in range(2,n+1,1):
        f*=i
    return f
    

def ler_inteiro():
    i=input('mensagem: ')
    return i
    
    
def cronometro(s):
    for i in range(s,-1,-1):
        print ("%d segundos" %i)
        
