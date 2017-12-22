from minha_bib import *

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
    
    
    
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
cont=0
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
if s=='X':
    X='humano'
    O='computador'
sorteio = sorteio (nome)
    

    
        
        
    