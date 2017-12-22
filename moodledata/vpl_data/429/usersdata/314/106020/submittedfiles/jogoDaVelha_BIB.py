# -*- coding: utf-8 -*-
# Minha bib
import random

simbolos = ['X', 'O']
posicoesValidas = [0, 1, 2]




tabuleiro=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
nomeJogador = ''
simboloJogador = ''
simboloComputador = ''



def solicitaSimboloDoHumano ():
    global simboloJogador
    global simboloComputador
    while True :
        simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ').upper()
        if (simboloJogador.upper() in simbolos ):
            break
            
    if simboloJogador == 'X':
        simboloComputador = 'O'
    else:
        simboloComputador = 'X'


def jogadaComputador():
    global tabuleiro
    while True:
        jogada =  [random.choice(posicoesValidas),random.choice(posicoesValidas)]
        if validaJogada(jogada):
            tabuleiro[jogada[0]][jogada[1]]=simboloComputador
            break
        
    
    
def validaJogada(jogada):
    if tabuleiro[jogada[0]][jogada[1]] == ' ':
        return True 
    
    
    
    
def jogadaHumanaValida(jogada):
    
    
    
    
    
    
    
    
def jogadaHumana():
    global tabuleiro
    jogada =int(input('Qual sua jogada, {}?' .format(nomeJogador)).split())
    
    
    while True:
    
            
            break 
    
    
    
    
    

def mostraTabuleiro():
    print(tabuleiro[0][0] + '|' + tabuleiro[0][1] + '|' + tabuleiro[0][2])
    print(tabuleiro[1][0] + '|' + tabuleiro[1][1] + '|' + tabuleiro[1][2])
    print(tabuleiro[2][0] + '|' + tabuleiro[2][1] + '|' + tabuleiro[2][2])
    
def sorteioPrimeiraJogada():
    return random.choice(['Humano', 'Computador'])
        



        
            

def zerar():
    pass
    




def jogar():
    global nomeJogador
    nomeJogador = input('Qual o seu nome (ou apelido)? ')
    solicitaSimboloDoHumano()
    quemJoga = sorteioPrimeiraJogada()
    print('Vencedor do sorteio para início do jogo: {}' .format(quemJoga))
    print(simboloJogador,simboloComputador)
    while True:
        if quemJoga=='Humano':
            jogadaHumana()
            mostraTabuleiro()
            quemJoga='Computador'
        else:
            jogadaComputador()
            mostraTabuleiro()
            quemJoga='Humano'
            
            
            
            
            
            
    
    
    
    




        
        