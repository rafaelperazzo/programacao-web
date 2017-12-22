# -*- coding: utf-8 -*-
from random import randint
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI

#Solicita nome 
#Retorno: Nome do usuário
def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome (ou apelido)? '))
    return nome
 
#solicita simbolo 
#Retorno: Array = [Simbolo do humano, simbolo do computador]
def solicitaSimboloDoHumano():
    simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    while simbolo not in ('X','O'):
        simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    if simbolo== 'X':
        scomputador='O'
    else:
        scomputador='X'
    return [simbolo, scomputador]

#Sorteio 
#Parâmetro: Nome dos jogadores e tabela
#Retorno: Retorna o resultado do sorteio (0 ou 1)
def sorteioPrimeiraJogada(nomes):
    resultado = randint(0, 1)
    print('Vencedor do sorteio para inicio do jogo: %s' % nomes[resultado][0])
    return resultado

#valida jogada
#Paraâmetro: Nome dos jogadores e tabela
#Retorno: Verdadeiro ou falso
def validaJogada(jogada, visual):
    if (visual[int(jogada[0])][int(jogada[2])] == ' '):
        return False
    else:
        return True

#jogada humana    
#Parâmetro: Nome dos jogadores e tabela
#Retorno: Tabela modificada    
def jogadaHumana(nome, visual):
    jogada = input('Qual sua jogada, %s: ' % nome[0])
    while validaJogada(jogada, visual):
        print('OPS!!! Essa jogada não está disponível. Tente novamente!')
        jogada = input('Qual sua jogada, %s: ' % nome[0])
    visual[int(jogada[0])][int(jogada[2])] = nome[1]
    return visual

#jogada do computador 
#Parâmetro: Nome dos jogadores e tabela
#Retorno: Tabela modificada
def jogadaComputador(nome, visual):
    jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    while validaJogada(jogada, visual):
        jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    visual[int(jogada[0])][int(jogada[2])] = nome[1]
    return visual

#mostrar tabuleiro   
#Parâmetro: tabela para ser mostrada
def mostraTabuleiro(visual):
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))
        
#Pergunta se deseja jogar novamente
#Retorno: Verdadeiro ou falso
def jogarNovamente():
    x = input('Deseja jogar novamente? (S ou N) ')
    if x == 'n':
        return True
    else:
        return False
        
#Verifica se há vencedor
#Parâmetro: Recebe a tabela para verificar
#Retorno: Retorna o simbolo do vencedor
def verificaVencedor(tabela):
    for a in range(0, 3):
            if tabela[0][a]==tabela[1][a]==tabela[2][a]:
                return tabela[1][a]
            if tabela[a][0]==tabela[a][1]==tabela[a][2]:
                return tabela[a][0]
    if (tabela[0][0]==tabela[1][1]==tabela[2][2]) or (tabela[2][0]==tabela[1][1]==tabela[0][2]):
        return tabela[1][1]
        
    return ' '