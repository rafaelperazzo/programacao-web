# -*- coding: utf-8 -*-
from datetime import datetime
# autenticação do simbolo para a jogada humano 

def simb_humano():
    simbH= input("Olá humano, informe o simbolo que deseja utilizar para a partida: X ou O :  ")
    while simbH!="X" and simbH!="x" and simbH!="O" and  simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
   
#sorteio
def sorteio ():
    now= datetime.now()
    a=now.minute
    if a%2==0:
        print("Quem inicia a partida, é você... Boa jogada")
    else:
        print("Quem inicia a partida, é máquina. Observe.")


#Função para printar os simbolos no tabuleiro:
def printarSimb():
    print (tabuleiro[0][0] +'|'+ tabuleiro[0][1] + '|'+ tabuleiro[0][2])
    print (tabuleiro[1][0] +'|'+ tabuleiro[1][1] + '|'+ tabuleiro[1][2])
    print (tabuleiro[2][0] +'|'+ tabuleiro[2][1] + '|'+ tabuleiro[2][2])

        
        
        
        

        
        
        
        

