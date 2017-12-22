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


print ('***Sejam bem vindos ao Jogo da velha do grupo de João Artur, Davi Alves e Júlia Moraes.***')

#Aqui começa o jogo
while True:	
	Computador = str('Computador')
	tabuleiro = [' ']*23
	#Nome
	nome_ok = False
	while nome_ok == False:        
			nome=input('Qual é o seu nome(ou apelido)? ')
			if nome:
				nome_ok = True

            
	lista = [nome, Computador]
	variavel = solicitaSimboloDoHumano()
	jogadorlet, computadorlet = listaLetra()
	vez = sorteioPrimeiraJogada(lista)
	print ('A partida começará por %s.' %vez)
	jogoAcontecendo = True
	while jogoAcontecendo:
		if vez == nome:
			posicaoTabuleiro()
			desenhoDoTabuleiro(tabuleiro)
			jogada = jogadaHumana()
			movimento = validaJogada(tabuleiro)
			defineJogada(tabuleiro,jogadorlet,movimento)
			if verificaVencedor(tabuleiro, jogadorlet):
				posicaoTabuleiro()
				desenhoDoTabuleiro(tabuleiro)
				print('Vencedor: %s' %nome)
				jogoAcontecendo = False
			else:
				if verificaVelha(tabuleiro):
					desenhoDoTabuleiro(tabuleiro)
					print('Deu velha!')
					break                    

				else:
					vez = Computador
					
		else:
			
			jogada = jogadaComputador(tabuleiro, computadorlet)
			defineJogada(tabuleiro, computadorlet, jogada)
			
			if verificaVencedor(tabuleiro, computadorlet):
				posicaoTabuleiro()
				desenhoDoTabuleiro(tabuleiro)
				print('Vencedor: Computador')
				jogoAcontecendo = False
			else:
				if verificaVelha(tabuleiro):					
					desenhoDoTabuleiro(tabuleiro)
					print('Deu velha!')
					break
				else:
					vez = nome
					
	if not jogarNovamente():
		break