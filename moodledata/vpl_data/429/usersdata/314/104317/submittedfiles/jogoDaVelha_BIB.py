# -*- coding: utf-8 -*-
# Minha bib
tabuleiro=[['','',''],['','',''],['','','']]


def solicitaSimboloDoHumano ():
    simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')
    while (simboloJogador != 'O')  and  (simboloJogador != 'X'):
        simboloJogador = input('Qual simbolo deseja ultilizar no jogo? ')
    return simboloJogador

def mostraTabuleiro():
    print(tabuleiro[0][0] + ' | ' + tabuleiro[0][1] + ' | ' + tabuleiro[0][2])
    print(tabuleiro[1][0] + ' | ' + tabuleiro[1][1] + ' | ' + tabuleiro[1][2])
    print(tabuleiro[2][0] + ' | ' + tabuleiro[2][1] + ' | ' + tabuleiro[2][2])
    
def sorteioPrimeiraJogada():
    humano=1
    computador=0
    sorteio=random.randint(0,1)
    if sorteio==1:
        print('Vencendor do sorteio para inicio do jogo:Humano')
    else:
        print('Vencendor do sorteio para inicio do jogo:Computador')
        


def jogadaHumana():
    for i in tabuleiro(3):
        for j in tabuleiro(3):
            tabuleiro.append(simboloJogador)
        
            
    
    




        
        