# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def solicitaSimboloDoHumano(symh,simb):
    if symh == "X":
        simb[0] = "X"
        simb[1] = "O"
        return ([simb[0],simb[1]])
    if symh == "O":
        simb[0] = "O"
        simb[1] = "X"
        return ([simb[0],simb[1]])
    else:
        print("Símbolo inválido!" )
        symh=str(input("Qual símbolo você deseja utilizar no jogo? "))
        return solicitaSimboloDoHumano(symh,simb)