# -*- coding: utf-8 -*-
from datetime import datetime
# autenticação do simbolo para a jogada humano 

def solicitaSimboloDoHumano():
  #  nome=input('Qual seu nome(ou apelido)? ')
    simbH= input("Qual o simbolo que você deseja utilizar no jogo? ")
    while simbH!="X" and simbH!="x" and simbH!="O" and  simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
   
#sorteio
def sorteioPrimeiraJogada ():
    now= datetime.now()
    a=now.second
    if a%2==0:
        print("Vencedor do sorteio para inicio do jogo: Computador")
        
        # chamar a função printartab com a jogada do computador
        
    else:
        print("Vencedor do sorteio para inicio do jogo: Jogador")
        #apos disso perguntar a posição desejada e printartab


#Função para printar o tabuleiro:
def mostraTabuleiro():
    tabuleiro=[['','',''],['','',''],['','','']]
    print (tabuleiro[0][0] +'|'+ tabuleiro[0][1] + '|'+ tabuleiro[0][2])
    print (tabuleiro[1][0] +'|'+ tabuleiro[1][1] + '|'+ tabuleiro[1][2])
    print (tabuleiro[2][0] +'|'+ tabuleiro[2][1] + '|'+ tabuleiro[2][2])
#Função da jogado do humano

def jogadaHumana(nome):
    print(" Qual a sua jogada, %s ?" %nome)
    
    
    
#Função para validar uma jogada
#def validarJogada():
    
    
    
#Função da Jogada do computador
#def jogadaComputador():


#Função que verifica o vencedor
#def verificaVencedor():
        
        
        
        

        
        
        
        

