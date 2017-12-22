# -*- coding: utf-8 -*-
from datetime import datetime
from random import randint
# autenticação do simbolo para a jogada humano 

def solicitaSimboloDoHumano():
  #  nome=input('Qual seu nome(ou apelido)? ')
    simbH= (input("\nQual o simbolo que você deseja utilizar no jogo? "))
    while simbH!="X" and simbH!="O" and simbH!="o" and simbH!="x" :
        print ("\nOps! Simbolo inválido")
        simbH= input("\nInforme um simbolo válido que deseja utilizar para a partida: X ou O :  ")
    if simbH=="X" or simbH=="x":
        simbH="X"
    else:
        simbH="O"
    return simbH
   
#sorteio
def sorteioPrimeiraJogada (simbM, simbH, tabuleiro, nome):
    now= datetime.now()
    a=now.second
    #essa var serve para ajudar a definir de quem será aproxima jogada 
    pro=0
    if a%2==0:
        print("\nVencedor do sorteio para inicio do jogo: Computador")
        prop=1
        # chama a função mostraTabuleiro com a jogada do computador
        tabuleiro=jogadaComputador(tabuleiro, simbM)
        mostraTabuleiro(tabuleiro)
        
        
    else:
        print("\nVencedor do sorteio para inicio do jogo: %s" %nome)
        prop=2
        #chama a função mostraTabuleiro com a jogada do jogador 
        #tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        
    return prop

#Função para printar o tabuleiro:

def mostraTabuleiro(tabuleiro):
    print(' ')
    print ('            ' + tabuleiro[0][0] +' | '+ tabuleiro[0][1] + ' | '+ tabuleiro[0][2])
    print ('            ' + tabuleiro[1][0] +' | '+ tabuleiro[1][1] + ' | '+ tabuleiro[1][2])
    print ('            ' + tabuleiro[2][0] +' | '+ tabuleiro[2][1] + ' | '+ tabuleiro[2][2])


#Função da jogada do humano

def jogadaHumana(nome, simbH, tabuleiro):
    casa=[]
    casa=input("\n Qual a sua jogada, %s ? " %nome)
    
    i=(casa[0])
    j=(casa[2])
    
    while i!="2" and i!="1" and i!="0" and j!='2' and j!='1' and j!='0' :
        print('\nOps! Jogada invalida... ')
        casa=int(input("\n Qual a sua jogada, %s ?" %nome))
        i=(casa[0])
        j=(casa[2])
    #tabuleiro[casa//10][casa%10]=simbH
    i=int(casa[0])
    j=int(casa[2])
        
    validarJogada(nome, simbH, tabuleiro, i, j)
    return tabuleiro
    
    
    
    
#Função para validar uma jogada
def validarJogada(nome, simbH, tabuleiro, i, j):
    if tabuleiro[i][j]!="X" and tabuleiro[i][j]!="O" :
        tabuleiro[i][j]=simbH
       
    else:
        print ("\nOPS!!! Essa jogada não está disponível. Tente novamente!")
        jogadaHumana(nome, simbH, tabuleiro) 
    
    
#Função da Jogada do computador

def jogadaComputador(tabuleiro, simbM):
    sortL=randint(0, 2)
    sortC=randint(0, 2)
    while tabuleiro[sortL][sortC] !=" " : 
        sortL=randint(0, 2)
        sortC=randint(0, 2)
    tabuleiro[sortL][sortC]=simbM
    return tabuleiro 
    

#Função que verifica o vencedor 
def VerificaVencedor(tab, simbH, nome, simbM):
    x=1
    if tab[0][0]==tab[0][2] and tab[0][0]==tab[0][1] and tab[0][1]==tab[0][2]:
        if tab[0][0]==simbH:
            x=2
        elif tab[0][0]==simbM:
            x=4
    elif tab[1][0]==tab[1][1] and tab[1][1]==tab[1][2] and tab[1][0]==tab[1][2]:
        if tab[1][0]==simbH:
            x=2
        elif tab[1][0]==simbM:
            x=4
    elif tab[2][0]==tab[2][1] and tab[2][1]==tab[2][2] and tab[2][0]==tab[2][2]:
        if tab[2][0]==simbH:
             x=2
        elif tab[2][0]==simbM:
            x=4
    elif tab[0][0]==tab[1][0] and tab[2][0]==tab[0][0] and tab[2][0]==tab[1][0]:
        if tab[1][0]==simbH:
            x=2
        elif tab[1][0]==simbM:
            x=4
    elif tab[0][1]==tab[1][1] and tab[1][1]==tab[2][1] and tab[0][1]==tab[2][1]:
        if tab[1][1]==simbH:
            x=2
        elif tab[1][1]==simbM:
            x=4
    elif tab[0][2]==tab[1][2] and tab[1][2]==tab[2][2] and tab[0][2]==tab[2][2]:
        if tab[2][2]==simbH:
            x=2
        elif tab[2][2]==simbM:
            x=4
    elif tab[0][0]==tab[1][1] and tab[1][1]==tab[2][2] and tab[0][0]==tab[2][2]:
        if tab[0][0]==simbH:
            x=2
        elif tab[0][0]==simbM:
            x=4
    elif tab[0][2]==tab[1][1] and tab[1][1]==tab[2][0] and tab[2][0]==tab[0][2]:
        if tab[2][0]==simbH:
            x=2
        elif tab[2][0]==simbM:
            x=4
    elif tab[0][0]!=" " and tab[0][1]!=" " and tab[0][2]!=" " and tab[1][0]!=" " and tab[1][1]!=" " and tab[1][2]!=" " and tab[2][0]!=" " and tab[2][1]!=" " and tab[2][2]!=" ":
         print ('Deu velha')
         x=6
    return x
    


