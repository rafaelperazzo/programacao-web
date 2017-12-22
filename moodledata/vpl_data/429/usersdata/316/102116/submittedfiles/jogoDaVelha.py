# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
#-*- coding: utf-8 -*-
'''
|***********************************************************************|
|Equipe: João Artur Pinheiro, Davi Alves de Moura e Júlia Moraes Pereira|
|Números de Matrícula: 405978, 405419, 405987                           |
|Jogo da Velha em Pyhton                                                |
|Turma: EM0006*2017.2 Professor: Maxwell Guimarães                      |
|Python 3.6                                                             |
|***********************************************************************|
'''
import random
import sys

print ('***Sejam bem vindos ao Jogo da velha do grupo de João Artur, Davi Alves e Júlia Moraes.***')
Computador = str('Computador')
#tabuleiro = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22']





#FUNÇÕES

#Sorteio da primeira jogada

def sorteioPrimeiraJogada(lista):
	sorteio=random.choice(lista)
	return sorteio



#Tabuleiro
def desenhoDoTabuleiro(espaco):    
    print('      |      |')
    print('   ' + str(espaco[0]) + '  |   ' + str(espaco[1]) + '  | ' + str(espaco[2]))
    print('      |      |')
    print('--------------------')
    print('      |      |')
    print('   ' + str(espaco[10]) + '  |   ' + str(espaco[11]) + '  | ' + str(espaco[12]))
    print('      |      |')
    print('--------------------')
    print('      |      |')
    print('   ' + str(espaco[20]) + '  |   ' + str(espaco[21]) + '  | ' + str(espaco[22]))
    print('      |      |')
     


#Variável
def solicitaSimboloDoHumano ():
    while True:
        variavel=str(input('Com qual símbolo você prefere jogar(X ou O)? ')).upper()
        if variavel== 'X' or variavel=='x' :
            print('Você jogará contra o computador, que usará O.')
            break
        elif variavel== 'O' or variavel=='o':
            print('Você jogará contra o computador, que usará X.')
            break
        else:        
            print('Você não digitou um símbolo válido.')
    return variavel
#Função para criar uma lista definindo as variáveis para o usuário e o computador
def listaLetra():
	global variavel
	if variavel== 'X' or variavel=='x':
		letra = ['X','O']
	elif variavel== 'O' or variavel=='o' or variavel=='0':
		letra= ['O','X']
	return letra
#Função para jogar sem precisar fechar
def jogarNovamente():
    print('Você quer jogar novamente?(sim ou não)')
    return input().lower().startswith('s')
       
def defineJogada(espaco, letra, jogada):
    espaco[jogada] =(''+letra+'')


#Jogada vencedora
def verificaVencedor(ep, var):
    
    return ((ep[0] == var and ep[1] == var and ep[2] == var) or 
    (ep[10] == var and ep[11] == var and ep[12] == var) or 
    (ep[20] == var and ep[21] == var and ep[22] == var) or 
    (ep[0] == var and ep[10] == var and ep[20] == var) or 
    (ep[1] == var and ep[11] == var and ep[21] == var) or 
    (ep[2] == var and ep[12] == var and ep[22] == var) or 
    (ep[0] == var and ep[11] == var and ep[22] == var) or 
    (ep[2] == var and ep[11] == var and ep[20] == var))

#Copia do tabuleiro

def copiaTabuleiro(espaco):
    
    copiaespaco = []

    for i in espaco:
        copiaespaco.append(i)

    return copiaespaco

#Verifica se há espaço livre no tabuleiro
def temEspacoLivre(espaco,jogada):	
	return espaco[jogada] == ' '

#recebe uma jogada do usuario

def jogadaHumana():
	print('Qual a sua jogada? (x e y[0,2])')
	jogada=input()
	return jogada

#Valida a jogada do usuário

def validaJogada(espaco):
	
	global jogada	
	while True:
		if jogada=='00' or jogada=='01' or jogada=='02' or jogada=='10' or jogada=='11' or jogada=='12' or jogada=='20' or jogada=='21' or jogada=='22' or temEspacoLivre(espaco, int(jogada)):
			break
		print('Você não digitou uma jogada válida.')
		jogada = jogadaHumana()
	return int(jogada)

def escolheJogadaAleatoriaDaLista(espaco, listaDeJogadas):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    jogadasPossiveis = []
    for i in listaDeJogadas:
        if temEspacoLivre(espaco, i):
            jogadasPossiveis.append(i)

    if len(jogadasPossiveis) != 0:
        return random.choice(jogadasPossiveis)
    else:
        return None

def jogadaComputador(espaco, computadorlet):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computadorlet == 'X':
        jogadorlet = 'O'
    else:
        jogadorlet = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(0, 23):
        copia = copiaTabuleiro(espaco)
        if temEspacoLivre(copia, i):
            defineJogada(copia, computadorlet, i)
            if verificaVencedor(copia, computadorlet):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(0, 23):
        copia = copiaTabuleiro(espaco)
        if temEspacoLivre(copia, i):
            defineJogada(copia, jogadorlet, i)
            if verificaVencedor(copia, jogadorlet):
                return i

    # Try to take one of the corners, if they are free.
    jogada = escolheJogadaAleatoriaDaLista(espaco, [0, 2, 20, 22])
    if jogada != None:
        return jogada

    # Try to take the center, if it is free.
    if temEspacoLivre(espaco, 11):
        return 11

    # Move on one of the sides.
    return escolheJogadaAleatoriaDaLista(espaco, [21, 10, 12, 1])
	
def tabuleiroCheio(espaco):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(0, 23):
        if temEspacoLivre(espaco, i):
            return False
    return True


while True:
	tabuleiro = [' ']*23
	#Nome

	nome_ok = False
	while nome_ok == False:        
			nome=input('Qual é o seu nome(ou apelido)? ')
			if nome:
				nome_ok=True

            
	lista= [nome, Computador]
	variavel=solicitaSimboloDoHumano()
	jogadorlet, computadorlet= listaLetra()
	vez=sorteioPrimeiraJogada(lista)
	print ('A partida começará por %s.' %vez)
	jogoAcontecendo=True
	while jogoAcontecendo:
		if vez==nome:
			desenhoDoTabuleiro(tabuleiro)
			jogada = jogadaHumana()
			movimento=validaJogada(tabuleiro)
			defineJogada(tabuleiro,variavel,movimento)
			if verificaVencedor(tabuleiro, jogadorlet):
				desenhoDoTabuleiro(tabuleiro)
				print('Vencedor: %s' %nome)
				jogoAcontecendo = False
			else:
				if tabuleiroCheio(tabuleiro):
					desenhoDoTabuleiro(tabuleiro)
					print('Deu velha!')
					break
				else:
					vez = Computador
					
		else:
			# Computer's turn.
			jogada = jogadaComputador(tabuleiro, computadorlet)
			defineJogada(tabuleiro, computadorlet, jogada)
			
			if verificaVencedor(tabuleiro, computadorlet):
				desenhoDoTabuleiro(tabuleiro)
				print('Vencedor: Computador')
				jogoAcontecendo = False
			else:
				if tabuleiroCheio(tabuleiro):
					desenhoDoTabuleiro(tabuleiro)
					print('Deu velha!')
					break
				else:
					vez = nome
					
	if not jogarNovamente():
		break

		
        
        

