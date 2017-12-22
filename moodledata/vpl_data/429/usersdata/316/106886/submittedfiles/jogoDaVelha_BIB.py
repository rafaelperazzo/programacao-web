# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random
import sys
import time


#FUNÇÕES

#Sorteio da primeira jogada

def sorteioPrimeiraJogada(lista):
	sorteio=random.choice(lista)
	return sorteio



#Tabuleiro
def mostraTabuleiro(espaco):    
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
#Desenha o tabuleiro mostrando as posições     
def posicaoTabuleiro():
         
    print('      |      |')
    print('  ' '00' '  |  ''01' '  | ' '02')
    print('      |      |')
    print('--------------------')
    print('      |      |')
    print('  ' '10' '  |  ''11' '  | ' '12')
    print('      |      |')
    print('--------------------')
    print('      |      |')
    print('  ' '20' '  |  ''21' '  | ' '22')
    print('      |      |')
    print(' ')
    print(' ')
    
        
#Função que pede a letra com que o usuário quer jogar
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
	variavel=solicitaSimboloDoHumano()
	if variavel== 'X' or variavel=='x':
		letra = ['X','O']
	elif variavel== 'O' or variavel=='o' or variavel=='0':
		letra= ['O','X']
	return letra
#Função para jogar sem precisar fechar
def jogarNovamente():
    print('Você quer jogar novamente?(sim ou não)')
    jn=input().upper().startswith('SIM')
    while not jn:            
            print('Volte Sempre!')
            time.sleep(2)
            sys.exit()      
            
            return False
    return True    
        
#Função que coloca a letra do usuário ou do computador no espaço escolhido para jogar       
def defineJogada(espaco, letra, jogada):
    espaco[jogada] = letra
  
    


#Jogada vencedora
def verificaVencedor(espaco, letra):
    if espaco[0] == letra and espaco[1] == letra and espaco[2] == letra:
        return True
    if espaco[10] == letra and espaco[11] == letra and espaco[12] == letra:
        return True
    if espaco[20] == letra and espaco[21] == letra and espaco[22] == letra:
        return True
    if espaco[0] == letra and espaco[10] == letra and espaco[20] == letra:
        return True
    if espaco[1] == letra and espaco[11] == letra and espaco[21] == letra:
        return True
    if espaco[2] == letra and espaco[12] == letra and espaco[22] == letra:
        return True
    if espaco[0] == letra and espaco[11] == letra and espaco[22] == letra:
        return True
    if espaco[2] == letra and espaco[11] == letra and espaco[20] == letra:
        return True

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
	
	jogada=jogadaHumana()
	while jogada not in '00 01 02 10 11 12 20 21 22'.split() or not temEspacoLivre(espaco,int(jogada)):
		
		print('Você não digitou uma jogada válida.')
		jogada = jogadaHumana()
	return int(jogada)
#Função que analisa que jogadas ainda estão disponíveis, cria uma lista com elas e escolhe aleatóriamente uma delas
def escolheJogadaAleatoriaDasPossiveis(espaco, listaDeJogadas):
    
    jogadasPossiveis = []
    for i in listaDeJogadas:
        if temEspacoLivre(espaco, i):
            jogadasPossiveis.append(i)

    if len(jogadasPossiveis) != 0:
        return random.choice(jogadasPossiveis)
    else:
        return None
#Função que recebe a jogada do computador, de acordo com os espaços livres e método para vencer o usuário
def jogadaComputador(espaco, letraC):
    
    if letraC == 'X':
        letraJ = 'O'
    else:
        letraJ = 'X'

    
    for i in range(0, 23):
        copia = copiaTabuleiro(espaco)
        if temEspacoLivre(copia, i):
            defineJogada(copia, letraC, i)
            if verificaVencedor(copia, letraC):
                return i

    
    for i in range(0, 23):
        copia = copiaTabuleiro(espaco)
        if temEspacoLivre(copia, i):
            defineJogada(copia, letraJ, i)
            if verificaVencedor(copia, letraJ):
                return i

    
    jogada = escolheJogadaAleatoriaDasPossiveis(espaco, [0, 2, 20, 22])
    if jogada != None:
        return jogada

    
    if temEspacoLivre(espaco, 11):
            if jogada != None:
                    return 11
    if jogada != None:
        return escolheJogadaAleatoriaDasPossiveis(espaco, [21, 10, 12, 1])

    

#Função que verifica se não há mais espaços livres, ou seja, deu velha	
def verificaVelha(tabuleiro):
    
    if tabuleiro[0] != ' ' and tabuleiro[1] != ' ' and tabuleiro[2] != ' ' and tabuleiro[10] != ' ' and tabuleiro[11] != ' ' and tabuleiro[12] != ' ' and tabuleiro[20] != ' ' and tabuleiro[21] != ' ' and tabuleiro[22] != ' ':
        
        return True
