# -*- coding: utf-8 -*-
from datetime import datetime
from random import randint
# autenticação do simbolo para a jogada humano 

def solicitaSimboloDoHumano():
  #  nome=input('Qual seu nome(ou apelido)? ')
    simbH= (input("Qual o simbolo que você deseja utilizar no jogo? "))
    while simbH!="X" and simbH!="O" and simbH!="o" and simbH!="x" :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
    if simbH=="X" or simbH=="x":
        simbH="X"
    else:
        simbH=="O"
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
        #tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        
    return prop

#Função para printar o tabuleiro:

def mostraTabuleiro(tabuleiro):
    print (tabuleiro[0][0] +'|'+ tabuleiro[0][1] + '|'+ tabuleiro[0][2])
    print (tabuleiro[1][0] +'|'+ tabuleiro[1][1] + '|'+ tabuleiro[1][2])
    print (tabuleiro[2][0] +'|'+ tabuleiro[2][1] + '|'+ tabuleiro[2][2])


#Função da jogada do humano

def jogadaHumana(nome, simbH, tabuleiro):
    casa=[]
    casa=input(" Qual a sua jogada, %s ?" %nome)
    #tabuleiro[casa//10][casa%10]=simbH
    i=int(casa[0])
    j=int(casa[2])
    while i>2 or j>2 or i<0 or j<0 :
        print('Ops! Jogada invalida... ')
        casa=int(input(" Qual a sua jogada, %s ?" %nome))
        i=int(casa[0])
        j=int(casa[2])
        
    validarJogada(nome, simbH, tabuleiro, i, j)
    return tabuleiro
    
    
    
    
#Função para validar uma jogada
def validarJogada(nome, simbH, tabuleiro, i, j):
    if tabuleiro[i][j]!="X" and tabuleiro[i][j]!="O" :
        tabuleiro[i][j]=simbH
       
    else:
        print ("OPS!!! Essa jogada não está disponível. Tente novamente!")
        jogadaHumana(nome, simbH, tabuleiro) 
    
    
#Função da Jogada do computador
#def jogadaComputador(tabuleiro, simbM):
#    if tabuleiro 
    
    

#Função caso computador inicie o jogo
def jogada1computer(tabuleiro, simbM):
    sortL=randint(0, 2)
    sortC=randint(0, 2)
    while tabuleiro[sortL][sortC] !=" " : 
        sortL=randint(0, 2)
        sortC=randint(0, 2)
    tabuleiro[sortL][sortC]=simbM
    return tabuleiro 
    

#Função que verifica o vencedor 
def VerificaVencedor(tab, simbH, nome):
    if tab[0][0]==tab[0][2] and tab[0][0]==tab[0][1] and tab[0][1]==tab[0][2]:
        if tab[0][0]==simbH:
            x=2
        else:
            print("Vencedor: Máquina")
            x=4
    elif tab[1][0]==tab[1][1] and tab[1][1]==tab[1][2] and tab[1][0]==tab[1][2]:
        if tab[1][0]==simbH:
            x=2
        else:
            x=4
    elif tab[2][0]==tab[2][1] and tab[2][1]==tab[2][2] and tab[2][0]==tab[2][2]:
        if tab[2][0]==simbH:
             x=2
        else:
            x=4
    elif tab[0][0]==tab[1][0] and tab[2][0]==tab[0][0] and tab[2][0]==tab[1][0]:
       if tab[1][0]==simbH:
            x=2
        else:
            x=4
    elif tab[0][1]==tab[1][1] and tab[1][1]==tab[2][1] and tab[0][1]==tab[2][1]:
       if tab[1][1]==simbH:
            x=2
        else:
            x=4
    elif tab[0][2]==tab[1][2] and tab[1][2]==tab[2][2] and tab[0][2]==tab[2][2]:
        if tab[2][2]==simbH:
            x=2
        else:
            x=4
    elif tab[0][0]==tab[1][1] and tab[1][1]==tab[2][2] and tab[0][0]==tab[2][2]:
        if tab[0][0]==simbH:
            x=2
        else:
            x=4
    elif tab[0][2]==tab[1][1] and tab[1][1]==tab[2][0] and tab[2][0]==tab[0][2]:
        if tab[2][0]==simbH:
            x=2
        else:
            x=4
    elif tab[0][0]!=" " and tab[0][1]!=" " and tab[0][2]!=" " and tab[1][0]!=" " and tab[1][1]!=" " and tab[1][2]!=" " and tab[2][0]!=" " and tab[2][1]!=" " and tab[2][2]!=" ":
         print ('Deu velha')
         x=6
    else:
        x=1
        
return x
