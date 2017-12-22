# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
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
    jogada=validaJogada_H1 (jogada,nome)    
    m=[]
    lista0=[' ',' ',' ']
    lista1=[' ',' ',' ']
    lista2=[' ',' ',' ']
    if s=='X':
        if jogada=='0 0':
            lista0[0]='X'
        if jogada=='0 1':
            lista0[1]='X'
        if jogada=='0 2':
            lista0[2]='X'
        if jogada=='1 0':
            lista1[0]='X'
        if jogada=='1 1':
            lista1[1]='X'
        if jogada=='1 2':
            lista1[2]='X'
        if jogada=='2 0':
            lista2[0]='X'
        if jogada=='2 1':
            lista2[1]='X'
        if jogada=='2 2':
            lista2[2]='X'
    if s=='O':
        if jogada=='0 0':
            lista0[0]='O'
        if jogada=='0 1':
            lista0[1]='O'
        if jogada=='0 2':
            lista0[2]='O'
        if jogada=='1 0':
            lista1[0]='O'
        if jogada=='1 1':
            lista1[1]='O'
        if jogada=='1 2':
            lista1[2]='O'
        if jogada=='2 0':
            lista2[0]='O'
        if jogada=='2 1':
            lista2[1]='O'
        if jogada=='2 2':
            lista2[2]='O'
    m.append(lista0)
    m.append(lista1)
    m.append(lista2)
    return m

def jogadaHumana_2 (nome,s,m,cont):
    jogada=validaJogada_H2 (m,i,j,nome)
    lista_0=m[0]
    lista_1=m[1]
    lista_2=m[2]
    if s=='X':
        if jogada=='0 0':
            lista_0[0]='X'
        if jogada=='0 1':
            lista_0[1]='X'
        if jogada=='0 2':
            lista_0[2]='X'
        if jogada=='1 0':
            lista_1[0]='X'
        if jogada=='1 1':
            lista_1[1]='X'
        if jogada=='1 2':
            lista_1[2]='X'
        if jogada=='2 0':
            lista_2[0]='X'
        if jogada=='2 1':
            lista_2[1]='X'
        if jogada=='2 2':
            lista_2[2]='X'
    if s=='O':
        if jogada=='0 0':
            lista_0[0]='O'
        if jogada=='0 1':
            lista_0[1]='O'
        if jogada=='0 2':
            lista_0[2]='O'
        if jogada=='1 0':
            lista_1[0]='O'
        if jogada=='1 1':
            lista_1[1]='O'
        if jogada=='1 2':
            lista_1[2]='O'
        if jogada=='2 0':
            lista_2[0]='O'
        if jogada=='2 1':
            lista_2[1]='O'
        if jogada=='2 2':
            lista_2[2]='O'
    m.append(lista_0)
    m.append(lista_1)
    m.append(lista_2)
    return m
 
def validaJogada_H2 (m,i,j,nome):
    while (m[i][j]!=' '):
        jogada = str(input('Qual sua jogada, '+nome+'? '))
        if (jogada=='0 0' or jogada=='0 1' or jogada=='0 2' or jogada=='1 0' or jogada=='1 1'or jogada=='1 2' or jogada=='2 0' or jogada=='2 1' or jogada=='2 2'):
            i=jogada[0]
            j=jogada[2]
            i=int(i)
            j=int(j)
        if (jogada!='0 0' and jogada!='0 1' and jogada!='0 2' and jogada!='1 0' and jogada!='1 1'and jogada!='1 2' and jogada!='2 0' and jogada!='2 1' and jogada!='2 2'):
            print('OPS!!! Essa jogada não está disponível. Tente novamente!')    
            continue
        if m[i][j]!=' ':
            print('OPS!!! Essa jogada não está disponível. Tente novamente!')
    return jogada
 
def validaJogada_H1 (jogada,nome):
    while (jogada!='0 0' and jogada!='0 1' and jogada!='0 2' and jogada!='1 0' and jogada!='1 1'and jogada!='1 2' and jogada!='2 0' and jogada!='2 1' and jogada!='2 2'):
        print('OPS!!! Essa jogada não está disponível. Tente novamente!')
        jogada = str(input('Qual sua jogada, '+nome+'? '))
    return jogada
 
def mostraTabuleiro (m):
    return print("",m[0][0],"|",m[0][1],"|",m[0][2],"\n",m[1][0],"|",m[1][1],"|",m[1][2],"\n",m[2][0],"|",m[2][1],"|",m[2][2],"")

def sorteio_i ():
    global i 
    i = random.randint(0,2)
    return i
   
def sorteio_j ():
    global j 
    j = random.randint(0,2)
    return j
     
def jogadaComputador_1 (s,i,j,cont):
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
    lista_0=m[0]
    lista_1=m[1]
    lista_2=m[2]
    if s=='X':
        if i==0:
            if j==0:
                lista_0[0]='O'
            if j==1:
                lista_0[1]='O'
            if j==2:
                lista_0[2]='O'
       if i==1:
            if j==0:
                lista_1[0]='O'
            if j==1:
                lista_1[1]='O'
            if j==2:
                lista_1[2]='O'
        if i==2:
            if j==0:
                lista_2[0]='O'
            if j==1:
                lista_2[1]='O'
            if j==2:
                lista_2[2]='O'
    if s=='O':
        if i==0:
            if j==0:
                lista_0[0]='X'
            if j==1:
                lista_0[1]='X'
            if j==2:
                lista_0[2]='X'
        if i==1:
            if j==0:
                lista_1[0]='X'
            if j==1:
                lista_1[1]='X'
            if j==2:
                lista_1[2]='X'
        if i==2:
            if j==0:
                lista_2[0]='X'
            if j==1:
                lista_2[1]='X'
            if j==2:
                lista_2[2]='X'
    m.append(lista_0)
    m.append(lista_1)
    m.append(lista_2)
    return m
        
def verificaVencedor (s,m,nome,cont):
    vv=0
    if s=='X':
        if m[0][0]=='X' and m[0][1]=='X' and m[0][2]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[1][0]=='X' and m[1][1]=='X' and m[1][2]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[2][0]=='X' and m[2][1]=='X' and m[2][2]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][0]=='X' and m[1][0]=='X' and m[2][0]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][1]=='X' and m[1][1]=='X' and m[2][1]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][2]=='X' and m[1][2]=='X' and m[2][2]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][0]=='X' and m[1][1]=='X' and m[2][2]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][2]=='X' and m[1][1]=='X' and m[2][0]=='X':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][0]=='O' and m[0][1]=='O' and m[0][2]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[1][0]=='O' and m[1][1]=='O' and m[1][2]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[2][0]=='O' and m[2][1]=='O' and m[2][2]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[0][0]=='O' and m[1][0]=='O' and m[2][0]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[0][1]=='O' and m[1][1]=='O' and m[2][1]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[0][2]=='O' and m[1][2]=='O' and m[2][2]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[0][0]=='O' and m[1][1]=='O' and m[2][2]=='O':
            print('Vencedor: computador')
            vv+=10
        if m[0][2]=='O' and m[1][1]=='O' and m[2][0]=='O':
            print('Vencedor: computador')
            vv+=10
    if s=='O':
        if m[0][0]=='O' and m[0][1]=='O' and m[0][2]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[1][0]=='O' and m[1][1]=='O' and m[1][2]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[2][0]=='O' and m[2][1]=='O' and m[2][2]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][0]=='O' and m[1][0]=='O' and m[2][0]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][1]=='O' and m[1][1]=='O' and m[2][1]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][2]=='O' and m[1][2]=='O' and m[2][2]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][0]=='O' and m[1][1]=='O' and m[2][2]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][2]=='O' and m[1][1]=='O' and m[2][0]=='O':
            print('Vencedor: '+nome+'')
            vv+=10
        if m[0][0]=='X' and m[0][1]=='X' and m[0][2]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[1][0]=='X' and m[1][1]=='X' and m[1][2]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[2][0]=='X' and m[2][1]=='X' and m[2][2]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[0][0]=='X' and m[1][0]=='X' and m[2][0]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[0][1]=='X' and m[1][1]=='X' and m[2][1]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[0][2]=='X' and m[1][2]=='X' and m[2][2]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[0][0]=='X' and m[1][1]=='X' and m[2][2]=='X':
            print('Vencedor: computador')
            vv+=10
        if m[0][2]=='X' and m[1][1]=='X' and m[2][0]=='X':
            print('Vencedor: computador')
            vv+=10
    return vv
        