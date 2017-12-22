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


def jogadaComputador(simb, tab):
    lin = random.randint(0,2)
    col = random.randint(0,2)
    if tab[lin][col] == " " and 0<=lin<=2 and 0<=col<=2:
        tab[lin][col]=simb
    else:
        jogadaComputador(simb, tab)
    return tab
    

def jogadaHumana(play,simb,tab):
    lin = play//10
    col = play - lin*10
    tab[lin][col]=simb[0]
    return tab

def validaJogada(play, tab, name,):
    lin = play//10
    col = play - lin*10
    if tab[lin][col] == " " and 0<=lin<=2 and 0<=col<=2:
        return play
    else:
        print("Jogada inválida!")
        play=int(input("Qual a sua jogada, %s?: " %(name[0])))
        return validaJogada(play, tab, name)
    
def mostraTabuleiro(tab):
    print("| %s | %s | %s |" %(tab[0][0], tab[0][1], tab[0][2]))
    print("| %s | %s | %s |" %(tab[1][0], tab[1][1], tab[1][2]))
    print("| %s | %s | %s |" %(tab[2][0], tab[2][1], tab[2][2]))

def verificaVencedor(tab, simb, name):
    lol=false
    if tab[0][0] != " " and tab[0][0]==tab[0][1]==tab[0][2]:
        if tab[0][0]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[0][0]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[1][0] != " " and tab[1][0]==tab[1][1]==tab[1][2]:
        if tab[1][0]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[1][0]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[2][0] != " " and tab[2][0]==tab[2][1]==tab[2][2]:
        if tab[2][0]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[2][0]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[0][0] != " " and tab[0][0]==tab[1][0]==tab[2][0]:
        if tab[0][0]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[0][0]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[0][1] != " " and tab[0][1]==tab[1][1]==tab[2][1]:
        if tab[0][1]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[0][1]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[0][2] != " " and tab[0][2]==tab[1][2]==tab[2][2]:
        if tab[0][2]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[0][2]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[0][0] != " " and tab[0][0]==tab[1][1]==tab[2][2]:
        if tab[0][0]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[0][0]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    if tab[0][2] != " " and tab[0][2]==tab[1][1]==tab[2][0]:
        if tab[0][2]==simb[0]:
            print("Vencedor: %s" %(name[0]))
            lol = true
        if tab[0][2]==simb[1]:
            print("Vencedor: %s" %(name[1]))
            lol = true
    else:
        lol = false
    return lol
    
def verificavelha(tab):
    if tab[0][0]!= " " and tab[1][0]!= " " and tab[2][0]!= " " and tab[0][1]!= " " and tab[1][1]!= " " and tab[2][1]!= " " and tab[0][2]!= " " and tab[1][2]!= " " and tab[2][2]!= " ":
        print("Deu velha!")
        return true
    else:
        return false
    
