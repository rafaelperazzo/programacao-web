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
    
def jogadaHumana_1 (nome,s,cont):
    jogada = str(input('Qual sua jogada, '+nome+'? '))
    if cont==0:
        m=[]
        lista0=[' ',' ',' ']
        lista1=[' ',' ',' ']
        lista2=[' ',' ',' ']
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

def jogadaHumana_2 (nome,s,m,cont):
    jogada=validaJogada_H (m,i,j,nome)
    if cont!=0:
        lista_0=m[0]
        lista_1=m[1]
        lista_2=m[2]
        if s=='X':
            if jogada=='00':
                if lista_0[0]==' ':
                    lista_0[0]='X'
            if jogada=='01':
                if lista_0[1]==' ':
                    lista_0[1]='X'
            if jogada=='02':
                if lista_0[2]==' ':
                    lista_0[2]='X'
            if jogada=='10':
                if lista_1[0]==' ':
                    lista_1[0]='X'
            if jogada=='11':
                if lista_1[1]==' ':
                    lista_1[1]='X'
            if jogada=='12':
                if lista_1[2]==' ':
                    lista_1[2]='X'
            if jogada=='20':
                if lista_2[0]==' ':
                    lista_2[0]='X'
            if jogada=='21':
                if lista_2[1]==' ':
                    lista_2[1]='X'
            if jogada=='22':
                if lista_2[2]==' ':
                    lista_2[2]='X'
        if s=='O':
            if jogada=='00':
                if lista_0[0]==' ':
                    lista_0[0]='O'
            if jogada=='01':
                if lista_0[1]==' ':
                    lista_0[1]='O'
            if jogada=='02':
                if lista_0[2]==' ':
                    lista_0[2]='O'
            if jogada=='10':
                if lista_1[0]==' ':
                    lista_1[0]='O'
            if jogada=='11':
                if lista_1[1]==' ':
                    lista_1[1]='O'
            if jogada=='12':
                if lista_1[2]==' ':
                    lista_1[2]='O'
            if jogada=='20':
                if lista_2[0]==' ':
                    lista_2[0]='O'
            if jogada=='21':
                if lista_2[1]==' ':
                    lista_2[1]='O'
            if jogada=='22':
                if lista_2[2]==' ':
                    lista_2[2]='O'
        m.append(lista_0)
        m.append(lista_1)
        m.append(lista_2)
    return m

def validaJogada_H (m,i,j,nome):
    while (i!=0 or i!=1 or i!=2 or j!=0 or j!=1 or j!=2):
        jogada = str(input('Qual sua jogada, '+nome+'? '))
        i=jogada[0]
        j=jogada[1]
        i=int(i)
        j=int(j)
    if m[i][j]!=' ':
        continue
    return jogada

def validaJogada_H2 (m,i,j,nome):
    while (m[i][j]!=' '):
        jogada = str(input('Qual sua jogada, '+nome+'? '))
        i=jogada[0]
        j=jogada[1]
        i=int(i)
        j=int(j)
    return jogada
            
def mostraTabuleiro (m):
    return print("",m[0][0],"|",m[0][1],"|",m[0][2],"\n",m[1][0],"|",m[1][1],"|",m[1][2],"\n",m[2][0],"|",m[2][1],"|",m[2][2],"")

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
    
def jogadaComputador_1 (s,i,j,cont):
    if cont==0:
        m=[]
        lista0=[' ',' ',' ']
        lista1=[' ',' ',' ']
        lista2=[' ',' ',' ']
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
    return m
    
def jogadaComputador_2 (s,i,j,cont,m):
    if cont!=0:
        lista_0=m[0]
        lista_1=m[1]
        lista_2=m[2]
        if s=='X':
            if i==0:
                if j==0:
                    if lista_0[0]==' ':
                        lista_0[0]='O'
                if j==1:
                    if lista_0[1]==' ':
                        lista_0[1]='O'
                if j==2:
                    if lista_0[2]==' ':
                        lista_0[2]='O'
            if i==1:
                if j==0:
                    if lista_1[0]==' ':
                        lista_1[0]='O'
                if j==1:
                    if lista_1[1]==' ':
                        lista_1[1]='O'
                if j==2:
                    if lista_1[2]==' ':
                        lista_1[2]='O'
            if i==2:
                if j==0:
                    if lista_2[0]==' ':
                        lista_2[0]='O'
                if j==1:
                    if lista_2[1]==' ':
                        lista_2[1]='O'
                if j==2:
                    if lista_2[2]==' ':
                        lista_2[2]='O'
        if s=='O':
            if i==0:
                if j==0:
                    if lista_0[0]==' ':
                        lista_0[0]='X'
                if j==1:
                    if lista_0[1]==' ':
                        lista_0[1]='X'
                if j==2:
                    if lista_0[2]==' ':
                        lista_0[2]='X'
            if i==1:
                if j==0:
                    if lista_1[0]==' ':
                        lista_1[0]='X'
                if j==1:
                    if lista_1[1]==' ':
                        lista_1[1]='X'
                if j==2:
                    if lista_1[2]==' ':
                        lista_1[2]='X'
            if i==2:
                if j==0:
                    if lista_2[0]==' ':
                        lista_2[0]='X'
                if j==1:
                    if lista_2[1]==' ':
                        lista_2[1]='X'
                if j==2:
                    if lista_2[2]==' ':
                        lista_2[2]='X'
        m.append(lista_0)
        m.append(lista_1)
        m.append(lista_2)
    return m
        
def verificaVencedor (s,m,nome,cont):
    if s=='X':
        if m[0][0]=='X' and m[0][1]=='X' and m[0][2]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[1][0]=='X' and m[1][1]=='X' and m[1][2]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[2][0]=='X' and m[2][1]=='X' and m[2][2]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][0]=='X' and m[1][0]=='X' and m[2][0]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][1]=='X' and m[1][1]=='X' and m[2][1]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][2]=='X' and m[1][2]=='X' and m[2][2]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][0]=='X' and m[1][1]=='X' and m[2][2]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][2]=='X' and m[1][1]=='X' and m[2][0]=='X':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][0]=='O' and m[0][1]=='O' and m[0][2]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[1][0]=='O' and m[1][1]=='O' and m[1][2]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[2][0]=='O' and m[2][1]=='O' and m[2][2]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[0][0]=='O' and m[1][0]=='O' and m[2][0]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[0][1]=='O' and m[1][1]=='O' and m[2][1]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[0][2]=='O' and m[1][2]=='O' and m[2][2]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[0][0]=='O' and m[1][1]=='O' and m[2][2]=='O':
            print('Vencedor: computador')
            cont+=10
        if m[0][2]=='O' and m[1][1]=='O' and m[2][0]=='O':
            print('Vencedor: computador')
            cont+=10
    if s=='O':
        if m[0][0]=='O' and m[0][1]=='O' and m[0][2]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[1][0]=='O' and m[1][1]=='O' and m[1][2]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[2][0]=='O' and m[2][1]=='O' and m[2][2]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][0]=='O' and m[1][0]=='O' and m[2][0]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][1]=='O' and m[1][1]=='O' and m[2][1]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][2]=='O' and m[1][2]=='O' and m[2][2]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][0]=='O' and m[1][1]=='O' and m[2][2]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][2]=='O' and m[1][1]=='O' and m[2][0]=='O':
            print('Vencedor: '+nome+'')
            cont+=10
        if m[0][0]=='X' and m[0][1]=='X' and m[0][2]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[1][0]=='X' and m[1][1]=='X' and m[1][2]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[2][0]=='X' and m[2][1]=='X' and m[2][2]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[0][0]=='X' and m[1][0]=='X' and m[2][0]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[0][1]=='X' and m[1][1]=='X' and m[2][1]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[0][2]=='X' and m[1][2]=='X' and m[2][2]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[0][0]=='X' and m[1][1]=='X' and m[2][2]=='X':
            print('Vencedor: computador')
            cont+=10
        if m[0][2]=='X' and m[1][1]=='X' and m[2][0]=='X':
            print('Vencedor: computador')
            cont+=10
    return cont
      