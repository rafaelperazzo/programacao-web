# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
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
        
