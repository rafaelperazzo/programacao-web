# -*- coding: utf-8 -*-
from random import randint
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI

#Solicita nome 
def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome ou (apelido)? '))
    return nome
 
 #solicita simbolo   
def solicitaSimboloDoHumano():
    simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    while simbolo not in ('X','O'):
        simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    if simbolo== 'X':
        scomputador='O'
    else:
        scomputador='X'
    return [simbolo, scomputador]

#sorteio 
def sorteioPrimeiraJogada(nomes):
    resultado = randint(0, 1)
    print('Vencedor do sorteio: %s' % nomes[resultado][0])
    return resultado

#valida jogada
def validaJogada(jogada, visual):
    if (visual[int(jogada[0])][int(jogada[2])] == ' '):
        return False
    else:
        return True

#jogada humana        
def jogadaHumana(nome, visual):
    jogada = input('Escolha sua jogada, %s: ' % nome[0])
    while validaJogada(jogada, visual):
        print('Jogada inválida')
        jogada = input('Escolha sua jogada, %s: ' % nome[0])
    visual[int(jogada[0])][int(jogada[2])] = nome[1]
    return visual

#jogada do computador 
def jogadaComputador(nome, visual):
    jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    while validaJogada(jogada, visual):
        jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    visual[int(jogada[0])][int(jogada[2])] = nome[1]
    return visual

#mostrar tabuleiro    
def mostraTabuleiro(i, visual):
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))
        
#Pergunta se deseja jogar novamente
#Retorno: Verdadeiro ou falso
def jogarNovamente():
    x = input('Deseja jogar novamente? (S ou N) ')
    if x = 'n':
        return True
    else:
        return False
        
#Verifica se há vencedor
#Parâmetro: Recebe a tabela para verificar
#Retorno: Retorna o simbolo do vencedor
def 