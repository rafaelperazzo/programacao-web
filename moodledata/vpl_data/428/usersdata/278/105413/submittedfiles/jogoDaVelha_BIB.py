# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simbolo_escolhido ():
    s = str(input("Qual símbolo você deseja utilizar no jogo? "))
    while (s!="X" and s!="O"):
        print("Símbolo inválido! Tente novamente.")
        s = str(input("Qual símbolo (X ou O) você deseja utilizar no jogo? "))
    return s
        
        
import random     
def sorteio (nome):
    sorteio = random.randint(1, 2)
    if sorteio==1:
        print('Vencedor do sorteio para início do jogo: '+nome+'.')
    if sorteio==2:
        print("Vencedor do sorteio para início do jogo: computador.")
    return sorteio
    
def jogadaHumana (nome,s,m,cont):
    jogada = str(input('Qual sua jogada, '+nome+'? '))
    if cont!=0:
        if s=='X':
            if jogada=='00':
                i=0
                j=0
                m[0][0]='X'
            if jogada=='01':
                i=0
                j=1
                m[0][1]='X'
            if jogada=='02':
                i=0
                j=2
                m[0][2]='X'
            if jogada=='10':
                i=1
                j=0
                m[1][0]='X'
            if jogada=='11':
                i=1
                j=1
                m[1][1]='X'
            if jogada=='12':
                i=1
                j=2
                m[1][2]='X'
            if jogada=='20':
                i=2
                j=0
                m[2][0]='X'
            if jogada=='21':
                i=2
                j=1
                m[2][1]='X'
            if jogada=='22':
                i=2
                j=2
                m[2][2]='X'
        if s=='O':
            if jogada=='00':
                i=0
                j=0
                m[0][0]='O'
            if jogada=='01':
                i=0
                j=1
                m[0][1]='O'
            if jogada=='02':
                i=0
                j=2
                m[0][2]='O'
            if jogada=='10':
                i=1
                j=0
                m[1][0]='O'
            if jogada=='11':
                i=1
                j=1
                m[1][1]='O'
            if jogada=='12':
                i=1
                j=2
                m[1][2]='O'
            if jogada=='20':
                i=2
                j=0
                m[2][0]='O'
            if jogada=='21':
                i=2
                j=1
                m[2][1]='O'
            if jogada=='22':
                i=2
                j=2
                m[2][2]='O'
    if cont==0:
        if s=='X':
            if jogada=='00':
                i=0
                j=0
                m[0][0]='X'
            if jogada=='01':
                i=0
                j=1
                m[0][1]='X'
            if jogada=='02':
                i=0
                j=2
                m[0][2]='X'
            if jogada=='10':
                i=1
                j=0
                m[1][0]='X'
            if jogada=='11':
                i=1
                j=1
                m[1][1]='X'
            if jogada=='12':
                i=1
                j=2
                m[1][2]='X'
            if jogada=='20':
                i=2
                j=0
                m[2][0]='X'
            if jogada=='21':
                i=2
                j=1
                m[2][1]='X'
            if jogada=='22':
                i=2
                j=2
                m[2][2]='X'
        if s=='O':
            if jogada=='00':
                i=0
                j=0
                m[0][0]='O'
            if jogada=='01':
                i=0
                j=1
                m[0][1]='O'
            if jogada=='02':
                i=0
                j=2
                m[0][2]='O'
            if jogada=='10':
                i=1
                j=0
                m[1][0]='O'
            if jogada=='11':
                i=1
                j=1
                m[1][1]='O'
            if jogada=='12':
                i=1
                j=2
                m[1][2]='O'
            if jogada=='20':
                i=2
                j=0
                m[2][0]='O'
            if jogada=='21':
                i=2
                j=1
                m[2][1]='O'
            if jogada=='22':
                i=2
                j=2
                m[2][2]='O'
    return m

def validaJogada (s,i,j):
    vj=0
    if s==1:
        if m[i][j]==' ':
            vj+=1
        if m[i][j]!=' ':
            print("OPS!!! Essa jogada não está disponível. Tente novamente!")
            vj=0
    if s==2:
        if c==' ':
            vj+=1
    return vj
            
        
def mostraTabuleiro (m):
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
    
def jogadaComputador (s,i,j,cont,m):
    i=int(i)
    j=int(j)
    if cont==0:
        if s=='X':
            if i==0:
                if j==0:
                    m[2][0]='O'
                if j==1:
                    m[2][0]='O'
                if j==2:
                    m[2][0]='O'
            if i==1:
                if j==0:
                    m[2][0]='O'
                if j==1:
                    m[2][0]='O'
                if j==2:
                    m[2][0]='O'
            if i==2:
                if j==0:
                    m[2][0]='O'
                if j==1:
                    m[2][0]='O'
                if j==2:
                    m[2][0]='O'
        if s=='O':
            if i==0:
                if j==0:
                    m[2][2]='X'
                if j==1:
                    m[2][2]='X'
                if j==2:
                    m[2][2]='X'
            if i==1:
                if j==0:
                    m[2][2]='X'
                if j==1:
                    m[2][2]='X'
                if j==2:
                    m[2][2]='X'
            if i==2:
                if j==0:
                    m[2][2]='X'
                if j==1:
                    m[2][2]='X'
                if j==2:
                    m[2][2]='X'
    if cont!=0:
        if s=='X':
            if i==0:
                if j==0:
                    m[2][0]='O'
                if j==1:
                    m[2][0]='O'
                if j==2:
                    m[2][0]='O'
            if i==1:
                if j==0:
                    m[2][0]='O'
                if j==1:
                    m[2][0]='O'
                if j==2:
                    m[2][0]='O'
            if i==2:
                if j==0:
                    m[2][0]='O'
                if j==1:
                    m[2][0]='O'
                if j==2:
                    m[2][0]='O'
        if s=='O':
            if i==0:
                if j==0:
                    m[2][2]='X'
                if j==1:
                    m[2][2]='X'
                if j==2:
                    m[2][2]='X'
            if i==1:
                if j==0:
                    m[2][2]='X'
                if j==1:
                    m[2][2]='X'
                if j==2:
                    m[2][2]='X'
            if i==2:
                if j==0:
                    m[2][2]='X'
                if j==1:
                    m[2][2]='X'
                if j==2:
                    m[2][2]='X'
    return m
        
        
    
      