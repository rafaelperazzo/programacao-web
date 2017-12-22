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
    
def jogadaHumana (nome, s, m):
    jogada = int(input('Qual sua jogada, '+nome+'? '))
    if s=='X':
        if jogada=='00':
            c=m[0][0]
            m[0][0]='X'
        if jogada=='01':
            c=m[0][1]
            m[0][1]='X'
        if jogada=='02':
            c=m[0][2]
            m[0][2]='X'
        if jogada=='10':
            c=m[1][0]
            m[1][0]='X'
        if jogada=='11':
            c=m[1][1]
            m[1][1]='X'
        if jogada=='12':
            c=m[1][2]
            m[1][2]='X'
        if jogada=='20':
            c=m[2][0]
            m[2][0]='X'
        if jogada=='21':
            c=m[2][1]
            m[2][1]='X'
        if jogada=='22':
            c=m[2][2]
            m[2][2]='X'
        validaJogada (s,jogada,c)
    if s=='O':
        if jogada=='00':
            c=lista0[0]
            lista0[0]='O'
        if jogada=='01':
            c=lista0[1]
            lista0[1]='O'
        if jogada=='02':
            c=lista0[2]
            lista0[2]='O'
        if jogada=='10':
            c=lista1[0]
            lista1[0]='O'
        if jogada=='11':
            c=lista1[1]
            lista1[1]='O'
        if jogada=='12':
            c=lista1[2]
            lista1[2]='O'
        if jogada=='20':
            c=lista2[0]
            lista2[0]='O'
        if jogada=='21':
            c=lista2[1]
            lista2[1]='O'
        if jogada=='22':
            c=lista2[2]
            lista2[2]='O'
        validaJogada (s,jogada,c)
        m.append(lista0)
        m.append(lista1)
        m.append(lista2)
    return m

def validaJogada (s, jogada, c):
    if s==1:
        while (jogada!='00' and jogada!='01' and jogada!='02' and jogada!='10' and jogada!='11' and jogada!='12' and jogada!='20' and jogada!='21' and jogada!='22'):
            print("OPS!!! Essa jogada não está disponível. Tente novamente!")
        while(c!=' '):
            print("OPS!!! Essa jogada não está disponível. Tente novamente!")
    if s==2:
        while (c!=' '):
            
        
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
    
def jogadaComputador (s,i,j):
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
    c=m[i][j]
    return m
        
        
    
      