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


def sorteioPrimeiraJogada():
    sort = random.randint(0,1)
    if sort == 0:
        
    