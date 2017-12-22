# -*- coding: utf-8 -*-
from datetime import datetime
from random import randint
# autenticação do simbolo para a jogada humano 

def solicitaSimboloDoHumano():
  #  nome=input('Qual seu nome(ou apelido)? ')
    simbH= input("Qual o simbolo que você deseja utilizar no jogo? ")
    while simbH!="X" and simbH!="x" and simbH!="O" and  simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
    return simbH
   
#sorteio
def sorteioPrimeiraJogada (simbM, simbH, tabuleiro, nome):
    now= datetime.now()
    a=now.second
    #essa var serve para ajudar a definir de quem será aproxima jogada 
    pro=0
    if a%2==0:
        print("Vencedor do sorteio para inicio do jogo: Computador")
        prop=1
        # chama a função mostraTabuleiro com a jogada do computador
        tabuleiro=jogada1computer(tabuleiro, simbM)
        mostraTabuleiro(tabuleiro)
        
        
    else:
        print("Vencedor do sorteio para inicio do jogo: Jogador")
        prop=2
        #chama a função mostraTabuleiro com a jogada do jogador 
        tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        mostraTabuleiro(tabuleiro)
    return prop

#Função para printar o tabuleiro:

def mostraTabuleiro(tabuleiro):
    print (tabuleiro[0][0] +'|'+ tabuleiro[0][1] + '|'+ tabuleiro[0][2])
    print (tabuleiro[1][0] +'|'+ tabuleiro[1][1] + '|'+ tabuleiro[1][2])
    print (tabuleiro[2][0] +'|'+ tabuleiro[2][1] + '|'+ tabuleiro[2][2])


#Função da jogada do humano

def jogadaHumana(nome, simbH, tabuleiro):
    casa=int(input(" Qual a sua jogada, %s ?" %nome))
    tabuleiro[casa//10][casa%10]=simbH
    return tabuleiro
    
    
    
#Função para validar uma jogada
#def validarJogada():
    
    
    
#Função da Jogada do computador
#def jogadaComputador():
    

#Função caso computador inicie o jogo
def jogada1computer(tabuleiro, simbM):
    sortL=randint(0, 2)
    sortC=randint(0, 2)
    tabuleiro[sortL][sortC]=simbM
    return tabuleiro 
    

#Função que verifica o vencedor 
#def verificaVencedor():
    

