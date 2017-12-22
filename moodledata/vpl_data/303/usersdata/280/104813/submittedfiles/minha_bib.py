# -*- coding: utf-8 -*-
import random

#COMECE AQUI ABAIXO
def solicitaSimboloDoHumano(si):
    simb=[" ", " "]
    if si == "X":
        simb[0] = "X"
        simb[1] = "O"
        return ([simb[0],simb[1]])
    if si == "O":
        simb[0] = "O"
        simb[1] = "X"
        return ([simb[0],simb[1]])
    else:
        print("Símbolo inválido!" )
        si=str(input("Qual símbolo você deseja utilizar no jogo? "))
        return solicitaSimboloDoHumano(si)


def sorteioPrimeiraJogada(name):
    sort = random.randint(0,1)
    if sort == 0:
        return name[0]
    if sort == 1:
        return name[1]


def jogadaComputador(simb):
    lin = random.randint(0,2)
    col = random.randint(0,2)
    return (lin, col, simb[1])
    
def validaJogada(lin, col, simb, tab):
    if tab[lin][col] == " " and 0<=lin<=2 and 0<=col<=2:
        return simb
    else:
        print("OPS!!! Essa jogada não está disponível. Tente novamente!")
        return validaJogada(lin, col, simb, tab)

def jogadaHumana(play,simb):
    lin = play//10
    col = play - lin*10
    return (lin, col, simb[0])
    
def mostraTabuleiro(tab):
    print("| %s | %s | %s |" %(tab[0][0], tab[0][1], tab[0][2]))
    print("| %s | %s | %s |" %(tab[1][0], tab[1][1], tab[1][2]))
    print("| %s | %s | %s |" %(tab[2][0], tab[2][1], tab[2][2]))
