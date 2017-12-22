# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
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
    while movimento not in '1 2 3 4 5 6 7 8 9'.split():
        while vazio(tabuleiro, int(movimento)):
            movimento=input("\nQual a sua jogada? ")
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

    movimento = validajogada(tabuleiro, [1, 3, 7, 9])
    if movimento != None:
        return movimento

    if vazio(tabuleiro, 5):
        return 5

    return movAleatoria(tabuleiro, [2, 4, 6, 8])



def mostraTabuleiro(tabuleiro):
    mostTabuleiro = []

    for i in tabuleiro:
        mostTabuleiro.append(i)

    return mostTabuleiro


 


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




def validajogada(tabuleiro, movimentosList):
    movPossiveis = []
    for i in movimentosList:
        if vazio(tabuleiro, i):
            movPossiveis.append(i)

    if len(movPossiveis) != 0:
        return random.choice(movPossiveis)
    else:
        return None



    