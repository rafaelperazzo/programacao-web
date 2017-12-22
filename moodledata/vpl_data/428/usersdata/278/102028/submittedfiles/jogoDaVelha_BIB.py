# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simbolo_escolhido ():
    s = str(input("Qual símbolo você deseja utilizar no jogo? "))
    while (s!="X" and s!="O"):
        print("Símbolo inválido! Tente novamente.")
        s = str(input("Qual símbolo (X ou O) você deseja utilizar no jogo? "))
    return s
        
        
import random     
def sorteio ():
    sorteio = random.randint(1, 2)
    if sorteio==1:
        print("Vencedor do sorteio para início do jogo: humano.")
    if sorteio==2:
        print("Vencedor do sorteio para início do jogo: computador.")
    return sorteio
    
def jogadaHumana ():
    jogada = int(input("Qual sua jogada, "+nome+"? "))
    validaJogada ()
    jogada = "+s+"
    mostraTabuleiro ()
    
def jogadaComputador ():
    
    
#def validaJogada ():
    while (jogada<0 or jogada>2):
        print("OPS!!! Essa jogada não está disponível. Tente novamente!")
        
def mostraTabuleiro ():
    m=[]
    linhas=(0,1,2)
    colunas=(0,1,2)
    for i in range:
        for j in range:
            chave= str(i)+ ' ' + str(j)
            n.append(chave)
    print(m)
    return m
    
            
      