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
    vj=0
    jogada = str(input('Qual sua jogada, '+nome+'? '))
    if cont!=0:
        if s=='X':
            while (vj==0):
                if jogada=='00':
                    i=0
                    j=0
                    c=m[0][0]
                    m[0][0]='X'
                if jogada=='01':
                    i=0
                    j=1
                    c=m[0][1]
                    m[0][1]='X'
                if jogada=='02':
                    i=0
                    j=2
                    c=m[0][2]
                    m[0][2]='X'
                if jogada=='10':
                    i=1
                    j=0
                    c=m[1][0]
                    m[1][0]='X'
                if jogada=='11':
                    i=1
                    j=1
                    c=m[1][1]
                    m[1][1]='X'
                if jogada=='12':
                    i=1
                    j=2
                    c=m[1][2]
                    m[1][2]='X'
                if jogada=='20':
                    i=2
                    j=0
                    c=m[2][0]
                    m[2][0]='X'
                if jogada=='21':
                    i=2
                    j=1
                    c=m[2][1]
                    m[2][1]='X'
                if jogada=='22':
                    i=2
                    j=2
                    c=m[2][2]
                    m[2][2]='X'
                else:
                    i=3
                    j=3
                vj=validaJogada (s,i,j,c)
            if s=='O':
                if jogada=='00':
                    i=0
                    j=0
                    c=m[0][0]
                    m[0][0]='O'
                if jogada=='01':
                    i=0
                    j=1
                    c=m[0][1]
                    m[0][1]='O'
                if jogada=='02':
                    i=0
                    j=2
                    c=m[0][2]
                    m[0][2]='O'
                if jogada=='10':
                    i=1
                    j=0
                    c=m[1][0]
                    m[1][0]='O'
                if jogada=='11':
                    i=1
                    j=1
                    c=m[1][1]
                    m[1][1]='O'
                if jogada=='12':
                    i=1
                    j=2
                    c=m[1][2]
                    m[1][2]='O'
                if jogada=='20':
                    i=2
                    j=0
                    c=m[2][0]
                    m[2][0]='O'
                if jogada=='21':
                    i=2
                    j=1
                    c=m[2][1]
                    m[2][1]='O'
                if jogada=='22':
                    i=2
                    j=2
                    c=m[2][2]
                    m[2][2]='O'
                vj=validaJogada (s,i,j,c)
    if cont==0:
        lista0=[' ', ' ', ' ']
        lista1=[' ', ' ', ' ']
        lista2=[' ', ' ', ' ']
        m=[]
        if s=='X':
            if jogada=='00':
                lista0[0]='X'
            if jogada=='01':
                lista0[1]='X'
            if jogada=='02':
                lista0[2]='X'
            if jogada=='10':
                lista1[0]='X'
            if jogada=='11':
                lista1[1]='X'
            if jogada=='12':
                lista1[2]='X'
            if jogada=='20':
                lista2[0]='X'
            if jogada=='21':
                lista2[1]='X'
            if jogada=='22':
                lista2[2]='X'
        if s=='O':
            if jogada=='00':
                lista0[0]='O'
            if jogada=='01':
                lista0[1]='O'
            if jogada=='02':
                lista0[2]='O'
            if jogada=='10':
                lista1[0]='O'
            if jogada=='11':
                lista1[1]='O'
            if jogada=='12':
                lista1[2]='O'
            if jogada=='20':
                lista2[0]='O'
            if jogada=='21':
                lista2[1]='O'
            if jogada=='22':
                lista2[2]='O'
        m.append(lista0)
        m.append(lista1)
        m.append(lista2)
    return m

def validaJogada (s,i,j,c):
    vj=0
    if s==1:
        if c==' ':
            vj+=1
        if i!=2 and i!=1 and i!=0 and j!=2 and j!=1 and j!=0:
            vj-=1
            print("OPS!!! Essa jogada não está disponível. Tente novamente!")
        if c!=' ':
            print("OPS!!! Essa jogada não está disponível. Tente novamente!")
            vj-=1
    if s==2:
        if c==' ':
            vj+=1
        if i!=2 and i!=1 and i!=0 and j!=2 and j!=1 and j!=0:
            vj-=1
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
    if cont==0:
        lista0=[' ', ' ', ' ']
        lista1=[' ', ' ', ' ']
        lista2=[' ', ' ', ' ']
        m=[]
        if s=='X':
            if i==0:
                if j==0:
                    lista0[0]='O'
                if j==1:
                    lista0[1]='O'
                if j==2:
                    lista0[2]='O'
            if i==1:
                if j==0:
                    lista1[0]='O'
                if j==1:
                    lista1[1]='O'
                if j==2:
                    lista1[2]='O'
            if i==2:
                if j==0:
                    lista2[0]='O'
                if j==1:
                    lista2[1]='O'
                if j==2:
                    lista2[2]='O'
        if s=='O':
            if i==0:
                if j==0:
                    lista0[0]='X'
                if j==1:
                    lista0[1]='X'
                if j==2:
                    lista0[2]='X'
            if i==1:
                if j==0:
                    lista1[0]='X'
                if j==1:
                    lista1[1]='X'
                if j==2:
                    lista1[2]='X'
            if i==2:
                if j==0:
                    lista2[0]='X'
                if j==1:
                    lista2[1]='X'
                if j==2:
                    lista2[2]='X'
        m.append(lista0)
        m.append(lista1)
        m.append(lista2)
    if cont!=0:
        if s=='X':
            if i==0:
                if j==0:
                    c=m[0][0]
                    m[0][0]='O'
                if j==1:
                    c=m[0][1]
                    m[0][1]='O'
                if j==2:
                    c=m[0][2]
                    m[0][2]='O'
            if i==1:
                if j==0:
                    c=m[1][0]
                    m[1][0]='O'
                if j==1:
                    c=m[1][1]
                    m[1][1]='O'
                if j==2:
                    c=m[1][2]
                    m[1][2]='O'
            if i==2:
                if j==0:
                    c=m[2][0]
                    m[2][0]='O'
                if j==1:
                    c=m[2][1]
                    m[2][1]='O'
                if j==2:
                    c=m[2][2]
                    m[2][2]='O'
        if s=='O':
            if i==0:
                if j==0:
                    c=m[0][0]
                    m[0][0]='X'
                if j==1:
                    c=m[0][1]
                    m[0][1]='X'
                if j==2:
                    c=m[0][2]
                    m[0][2]='X'
            if i==1:
                if j==0:
                    c=m[1][0]
                    m[1][0]='X'
                if j==1:
                    c=m[1][1]
                    m[1][1]='X'
                if j==2:
                    c=m[1][2]
                    m[1][2]='X'
            if i==2:
                if j==0:
                    c=m[2][0]
                    m[2][0]='X'
                if j==1:
                    c=m[2][1]
                    m[2][1]='X'
                if j==2:
                    c=m[2][2]
                    m[2][2]='X'
        validaJogada (s,i,j,c)
    return m
        
        
    
      