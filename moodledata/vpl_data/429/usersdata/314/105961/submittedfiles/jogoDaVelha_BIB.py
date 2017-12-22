# -*- coding: utf-8 -*-
# Minha bib
import random

simbolos = ['X', 'O']
posicoesValidas = ['0','1','2']



global tabuleiro 
global nomeJogador
global simboloJogador 
global simboloComputador 



def solicitaSimboloDoHumano ():
    while True :
        simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ').upper()
        if (simboloJogador.upper() in simbolos ):
            break
            
    if simboloJogador == 'X':
        simboloComputador = 'O'
    else:
        simboloComputador = 'X'
    

def mostraTabuleiro():
    print(tabuleiro[0][0] + ' | ' + tabuleiro[0][1] + ' | ' + tabuleiro[0][2])
    print(tabuleiro[1][0] + ' | ' + tabuleiro[1][1] + ' | ' + tabuleiro[1][2])
    print(tabuleiro[2][0] + ' | ' + tabuleiro[2][1] + ' | ' + tabuleiro[2][2])
    
def sorteioPrimeiraJogada():
    return random.choice('Humano' , 'Computador')
        


def jogadaHumana():
    jogada = input('Qual sua jogada, {}?' .format(nomeJogador))
    validaJogada(jogada)    
        
            

def zerar():
    tabuleiro=[['','',''],['','',''],['','','']]
    nomeJogador = ''
    simboloJogador = ''
    simboloComputador = ''
    




def jogar():
   
    nomeJogador = input('Qual o seu nome (ou apelido)? ')
    solicitaSimboloDoHumano()
    print(simboloJogador,simboloComputador)
  
    
    
    
    




        
        