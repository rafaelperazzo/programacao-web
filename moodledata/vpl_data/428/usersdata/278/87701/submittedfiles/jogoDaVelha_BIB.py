# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simbolo_escolhido ():
    s = str(input("Qual símbolo você deseja utilizar no jogo? "))
    while (s!="X" and s!="O"):
        print("Símbolo inválido! Tente novamente.")
        s = str(input("Qual símbolo (X ou O) você deseja utilizar no jogo? "))
        
def sorteio ():
    if sorteio=="+nome+":
        print("Vencedor do sorteio para início do jogo: +nome+.")
    if sorteio=="computador":
        print("Vencedor do sorteio para início do jogo: computador.")
        
import random     
def sorteio ():
    sorteio = random.randint(1, 2)
    if sorteio==1:
        print("Vencedor do sorteio para início do jogo: humano.")
    if sorteio==2:
        print("Vencedor do sorteio para início do jogo: computador.")
        print("   |   |   ")
        print("   | O |   ")
        print("   |   |   ")