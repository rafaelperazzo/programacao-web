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

#def validaJogada ():
    while (jogada<0 or jogada>2):
        print("OPS!!! Essa jogada não está disponível. Tente novamente!")
        
def mostraTabuleiro (lista0,lista1,lista2):
    m=[]
    m.append(lista0)
    m.append(lista1)
    m.append(lista2)
    return print("",m[0][0],"|",m[0][1],"|",m[0][2],"\n",m[1][0],"|",m[1][1],"|",m[1][2],"\n",m[2][0],"|",m[2][1],"|",m[2][2])

import random
def sorteio_i ():
    global i 
    i = random.randint(0,2)
    print(i)
    return i
    
def sorteio_j ():
    global j 
    j = random.randint(0,2)
    print(j)
    return j
    
def jogadaComputador (i,j):
    lista0=[' ', ' ', ' ']
    lista1=[' ', ' ', ' ']
    lista2=[' ', ' ', ' ']
    lista0[0]=O
        
        
    
      