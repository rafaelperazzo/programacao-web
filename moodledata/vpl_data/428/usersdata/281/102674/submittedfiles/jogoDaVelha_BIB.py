# -*- coding: utf-8 -*-
import random
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
jogo_da_velha=[]

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
    jog_H=int(inpu("Digite sua jogada: "))
    
def jogadapc ():
    l0=[' ',' ',' ']
    l1=[' ',' ',' ']
    l2=[' ',' ',' ']
    sorte_pcL=random.randint(0,2)
    sorte_pcC=random.randint(0,2)
    if sim=='X':
        if sort_pcL==0 and sort_pcC==0:
            l0[0]='O'
        if sort_pcL==0 and sorte_pcC==1:
            l0[1]='O'
        if sort_pcL==0 and sorte_pcC==2:
            l0[2]='O'
        if sort_pcL==1 and sorte_pcC==0:
            l0[1]='O'
        if sort_pcL==1 and sorte_pcC==1:
            l0[1]='O'
        if sort_pcL==1 and sorte_pcC==2:
            l0[1]='O'
        if sort_pcL==2 and sorte_pcC==0:
            l0[1]='O'
        if sort_pcL==2 and sorte_pcC==1:
            l0[1]='O'
        if sort_pcL==2 and sorte_pcC==2:
            l0[1]='O'
        
            
    
