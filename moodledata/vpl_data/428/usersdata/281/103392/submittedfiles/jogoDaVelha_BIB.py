# -*- coding: utf-8 -*-
import random
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
jogo_da_velha=[]



def solicitaSimboloDoHumano():
    # Escolhe o símbolo
    
    simbolo = ''
    while not (simbolo == 'X' or simbolo == 'O'):
        print('Você quer ser X ou O?')
        simbolo = input().upper()

    # Define o símbolo do computador
    if simbolo == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
        
def simb ():
    simb= str(input('Qual o simbolo que voce quer ultilizar X ou O? '))
    while (simb != 'X' and simb != 'O'):
        print('Simbolo invalido')
        simb=str(input('Qual o simbolo que voce quer ultilizar X ou O? '))
    return(simb)

def sorteio ():
    sorteio=random.randint(0,1)
    return sorteio
    
def jogadahumano ():
    tab=[]
    jog_H=int(input("Digite sua jogada: "))
    
def jogadapc ():
    tab=[]
    l0=[' ',' ',' ']
    l1=[' ',' ',' ']
    l2=[' ',' ',' ']
    sorte_pcL=random.randint(0,2)
    sorte_pcC=random.randint(0,2)
    print(sorte_pcL)
    print(sorte_pcC)
    if simb=='X':
        if sort_pcL==0: 
            if sort_pcC==0:
                l0[0]='O'
        if sort_pcL==0: 
            if sort_pcC==1:
                l0[1]='O'
        if sort_pcL==0: 
            if sort_pcC==2:
                l0[2]='O'
        if sort_pcL==1: 
            if sort_pcC==0:
                l1[0]='O'
        if sort_pcL==1:
            if sort_pcC==1:
                l1[1]='O'
        if sort_pcL==1: 
            if sort_pcC==2:
                l1[2]='O'
        if sort_pcL==2: 
            if sort_pcC==0:
                l2[0]='O'
        if sort_pcL==2: 
            if sort_pcC==1:
                l2[1]='O'
        if sort_pcL==2: 
            if sort_pcC==2:
                l2[2]='O'
    tab.append(l0)
    tab.append(l1)
    tab.append(l2)
    print(tab)
    return tab
        
            
    
