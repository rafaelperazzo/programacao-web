# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome ou (apelido)? '))
    return nome
def solicitaSimboloDoHumano():
    simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    while simbolo not in ('X','O'):
        simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    if simbolo== 'X':
        scomputador='O'
    else:
        scomputador='X'
    return [simbolo, scomputador]
def grafico():
    visual = [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]  
    for i in range(0, 10, 1):
    a = str(input('Selecione a posição: '))
    if i%2==0:
        visual[int(a[0])][int(a[2])]='X'
    else: 
        visual[int(a[0])][int(a[2])]='O'
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))
nomes=[["a","d"],["Computador","k"]]
