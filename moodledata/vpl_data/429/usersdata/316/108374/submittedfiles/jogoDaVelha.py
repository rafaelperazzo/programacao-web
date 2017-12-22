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
from jogoDaVelha_BIB import *

print ('***Seja bem vindo ao Jogo da Velha do grupo de João Artur, Davi Alves e Júlia Moraes.***')

#Aqui começa o jogo
while True:	
	Computador = str('Computador')
	#Nome
	nome_ok = False
	while nome_ok == False:        
			nome=input('Qual é o seu nome(ou apelido)? ')
			if nome:
				nome_ok = True            
	lista = [nome, Computador]
	
	letraJ, letraC = listaLetra()
	vez = sorteioPrimeiraJogada(lista)
	print ('A partida começará por %s.' %vez)	
	tabuleiro = [' ']*23
	while True:
		if vez == nome:
			posicaoTabuleiro()
			mostraTabuleiro(tabuleiro)
			
			movimento = validaJogada(tabuleiro)
			defineJogada(tabuleiro,letraJ,movimento)
			if verificaVencedor(tabuleiro, letraJ):
				posicaoTabuleiro()
				mostraTabuleiro(tabuleiro)
				print('Vencedor: %s' %nome)
				break
			else:
				if verificaVelha(tabuleiro):
					mostraTabuleiro(tabuleiro)
					print('Deu velha!')
					break                    

				else:
					vez = Computador
					
		else:
			
			jogada = jogadaComputador(tabuleiro, letraC)
			defineJogada(tabuleiro, letraC, jogada)
			
			if verificaVencedor(tabuleiro, letraC):
				posicaoTabuleiro()
				mostraTabuleiro(tabuleiro)
				print('Vencedor: Computador')
				break
			else:
				if verificaVelha(tabuleiro):					
					mostraTabuleiro(tabuleiro)
					print('Deu velha!')
					break
				else:
					vez = nome
					
	if not jogarNovamente():
		break