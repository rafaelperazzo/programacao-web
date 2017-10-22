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
    
def simbolo_escolhido ():
    s = str(input("Qual símbolo você deseja utilizar no jogo? "))
    while (s!="X" and s!="O"):
        print("Símbolo inválido! Tente novamente.")
        s = str(input("Qual símbolo (X ou O) você deseja utilizar no jogo? "))
        
def sorteio ():
    

        