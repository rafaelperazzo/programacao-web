# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
import time

def hello_word():
    print("Olá mundo")
    return

def fatorial(n):
    f=1
    for i in range (2,n+1,1):
        f*=i
        print("Estou no %.d" %(f))
    return f
    
def cronometro(s):
    for i in range (s,0,-1):
        print("%.d" %(i))
        time.sleep(2)
        
def media(n1,n2):
    m=(n1+n2)/2.0
    return m
    
def ler_inteiro():
    i = int(input("Digite um inteiro: "))
    return i

def ler_carta_baralho():
    while (True):
        carta = ler_inteiro()
        if carta>=1 and carta<=13:
            break
        else:
            print("CARTA INVALIDA")
    return carta

import random    
def sorteioNatal ():
    s=random.randint('Florinda','Monteiro')
    print(s)
    
import random     
def sorteio (nome):
    sorteio = random.randint(1, 2)
    if sorteio==1:
        print('Vencedor do sorteio para início do jogo: '+nome+'.')
    if sorteio==2:
        print("Vencedor do sorteio para início do jogo: computador.")
    return sorteio
        