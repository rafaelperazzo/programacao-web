# -*- coding: utf-8 -*-
from datetime import datetime
# autenticação do simbolo para a jogada humano 

def simb_humano():
    nome=input('Qual seu nome(ou apelido)? ')
    simbH= input("Qual o simbolo que você deseja utilizar? ")
    while simbH!="X" and simbH!="x" and simbH!="O" and  simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
   
#sorteio
def sorteio ():
    now= datetime.now()
    a=now.second
    if a%2==0:
        print("Vencedor do sorteio para inicio do jogo: Computador")
        # chamar a função printartab com a jogada do computador
        
    else:
        print("Vencedor do sorteio para inicio do jogo: Jogador")#apos disso perguntar a posição desejada e printartab


#Função para printar o tabuleiro:
def printartab():
    print (tabuleiro[0][0] +'|'+ tabuleiro[0][1] + '|'+ tabuleiro[0][2])
    print (tabuleiro[1][0] +'|'+ tabuleiro[1][1] + '|'+ tabuleiro[1][2])
    print (tabuleiro[2][0] +'|'+ tabuleiro[2][1] + '|'+ tabuleiro[2][2])

        
        
        
        

        
        
        
        

