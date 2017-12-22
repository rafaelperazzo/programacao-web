# -*- coding: utf-8 -*-
import random
import time

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
    if play<0 or play>22:
        print("Jogada inválida!")
        play=int(input("Qual a sua jogada, %s?: " %(name[0])))
        return validaJogada(play, tab, name)
    else:
        lin = play//10
        col = play - lin*10
        if (lin<0 or lin>2) or (col<0 or col>2):
            print("Jogada inválida!")
            play=int(input("Qual a sua jogada, %s?: " %(name[0])))
            return validaJogada(play, tab, name)
        elif tab[lin][col] != " " :
            print("Jogada inválida!")
            play=int(input("Qual a sua jogada, %s?: " %(name[0])))
            return validaJogada(play, tab, name)
        else:
            return play
    
def mostraTabuleiro(tab):
    print("| %s | %s | %s |" %(tab[0][0], tab[0][1], tab[0][2]))
    print("| %s | %s | %s |" %(tab[1][0], tab[1][1], tab[1][2]))
    print("| %s | %s | %s |" %(tab[2][0], tab[2][1], tab[2][2]))

def verificaVencedor(tab, simb, name):
    lol=True
    if tab[0][0] != " " and tab[0][0]==tab[0][1]==tab[0][2]:
        lol=True
        if tab[0][0]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[0][0]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[1][0] != " " and tab[1][0]==tab[1][1]==tab[1][2]:
        lol=True
        if tab[1][0]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[1][0]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[2][0] != " " and tab[2][0]==tab[2][1]==tab[2][2]:
        lol=True
        if tab[2][0]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[2][0]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[0][0] != " " and tab[0][0]==tab[1][0]==tab[2][0]:
        lol=True
        if tab[0][0]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[0][0]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[0][1] != " " and tab[0][1]==tab[1][1]==tab[2][1]:
        lol=True
        if tab[0][1]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[0][1]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[0][2] != " " and tab[0][2]==tab[1][2]==tab[2][2]:
        lol=True
        if tab[0][2]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[0][2]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[0][0] != " " and tab[0][0]==tab[1][1]==tab[2][2]:
        lol=True
        if tab[0][0]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[0][0]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    elif tab[0][2] != " " and tab[0][2]==tab[1][1]==tab[2][0]:
        lol=True
        if tab[0][2]==simb[0]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[0]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        if tab[0][2]==simb[1]:
            time.sleep(1)
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Vencedor: %s" %(name[1]))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    else:
        lol=False
    return lol
    
def verificavelha(tab):
    lol=0
    if tab[0][0]!= " " and tab[1][0]!= " " and tab[2][0]!= " " and tab[0][1]!= " " and tab[1][1]!= " " and tab[2][1]!= " " and tab[0][2]!= " " and tab[1][2]!= " " and tab[2][2]!= " ":
        time.sleep(1)
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("        Deu velha!")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        lol=1
        return lol
    else:
        lol=0
        return lol

def jogadaboa(tab, simb):
    if tab[0][0]== " " and tab[1][0]== " " and tab[2][0]== " " and tab[0][1]== " " and tab[1][1]== " " and tab[2][1]== " " and tab[0][2]== " " and tab[1][2]== " " and tab[2][2]== " ":
        sort=random.randint(0,3)
        if sort == 0: 
            tab[0][0]=simb[1]
        if sort == 1:
            tab[0][2]=simb[1]
        if sort == 2:
            tab[2][0]=simb[1]
        if sort == 3:
            tab[2][2]=simb[1]
        return tab
    if tab[0][0]
    
    
