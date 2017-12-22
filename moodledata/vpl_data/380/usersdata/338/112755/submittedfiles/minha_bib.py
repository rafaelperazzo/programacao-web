"""

"""
from time import sleep
import random

def solicitaSimboloDoHumano(nome_do_jogador):
    simb = raw_input('Digite um simbolo para jogar [X ou O]: ')
    while(True):
        if simb == 'X' or simb == 'O' :
            break
        else:
            simb = raw_input('Digite um simbolo válido para jogar [X ou O]: ')
    return simb

def simbolodocomputador(simb):
    if simb == 'X' :
        simbC = 'O'
    if simb == 'O' :
        simbC = 'X'
    return simbC

def sorteioPrimeiraJogada(simb,simbC):
    a = random.choice([simb,simbC])
    if a == simb :        
        return  True
    if a == simbC :       
        return  False

def mostreTabuleiro():    
    print(" ")
    print(coordenadas[0][0]  + "|" + coordenadas[0][1] + ' ' + "|" + coordenadas[0][2]) 
    print('--+---+---')
    print(coordenadas[1][0]  + "|" + coordenadas[1][1] + ' ' + "|" + coordenadas[1][2])    #print coordenadas
    print('--+---+---')
    print(coordenadas[2][0]  + "|" + coordenadas[2][1] + ' ' + "|" + coordenadas[2][2])
    sleep(1)
    print(" ")
    print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
    print('---+--+---')
    print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])    #print tabuleiro
    print('---+--+---')
    print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])    


def jogadaHumana(jogadaH,simb):    
    i = jogadaH(0)
    j = jogadaH(1)
    
    while(True): 
        if int(jogadaH[0]) >= 0 and int(jogadaH[0]) < 3 :
            if int(jogadaH[1]) >= 0 and int(jogadaH[1]) < 3:
                if tabuleiro[i][j] != "X" and tabuleiro[i][j] != "O" :
                    break
        else:
            jogadaH = input('Digite uma jogada válida %s: ' % nome_do_jogador)
        tabuleiro[i][j] = simb
        return tabuleiro[i][j]
          
            
coordenadas = [
             ('00', '01', '02')
            ,('10', '11','12')  #Matriz das coordenadas
            ,('20','21','22')
            ]

tabuleiro = [
             (' ', ' ', ' ')
            ,(' ', ' ', ' ')  #matriz tabuleiro
            ,(' ', ' ', ' ')
            ]
      
tabuleiro = []
for i in range (3):
    v = []
    for j in range(3):
        v.append(' ')
    tabuleiro.append(v)

print('BEM VINDO AO JOGO DA VELHA')
nome_do_jogador = raw_input('Digite seu nome ou apelido: ')
simb = solicitaSimboloDoHumano(nome_do_jogador)
simbC = simbolodocomputador(simb)
print("O seu simbolo será o " + simb)
print('O simbolo do computador será o ' + simbC)
jogadaH = raw_input('Digite sua jogada %s : ' % nome_do_jogador)

if sorteioPrimeiraJogada(simb,simbC) == True :
    print('Você começa')
else:
    print('Computador começa')

mostreTabuleiro()
