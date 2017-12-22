# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome ou (apelido)? '))
    return nome
def solicitaSimboloDoHumano():
    simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    while simbolo not in ('X','x','o','O'):
        simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    if simbolo== 'X':
        scomputador='O'
    else:
        scomputador='X'
    return [simbolo, scomputador]
nomes=[["a","d"],["Computador","k"]]
print('Bem Vindo ao Jogo da Velha do Grupo "Deu Velha"')
nomes[0][0]=solicitaNomeDoJogador()
a=solicitaSimboloDoHumano()
nomes[0][1]=a[0]
nomes[1][1]=a[1]
print(nomes)
