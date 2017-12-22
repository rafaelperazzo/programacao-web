# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
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
    jn=input().lower().startswith('s')
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
	
	jogada=jogadaHumana()
	while jogada not in '00 01 02 10 11 12 20 21 22'.split() or not temEspacoLivre(espaco,int(jogada)):
		
		print('Você não digitou uma jogada válida.')
		jogada = jogadaHumana()
	return int(jogada)
#Função que analisa que jogadas ainda estão disponíveis e cria uma lista com elas
def escolheJogadaAleatoriaDaLista(espaco, listaDeJogadas):
    
    jogadasPossiveis = []
    for i in listaDeJogadas:
        if temEspacoLivre(espaco, i):
            jogadasPossiveis.append(i)

    if len(jogadasPossiveis) != 0:
        return random.choice(jogadasPossiveis)
    else:
        return None
#Função que recebe a jogada do computador, de acordo com os espaços livres e método para vencer o usuário
def jogadaComputador(espaco, computadorlet):
    
    if computadorlet == 'X':
        jogadorlet = 'O'
    else:
        jogadorlet = 'X'

    
    for i in range(0, 23):
        copia = copiaTabuleiro(espaco)
        if temEspacoLivre(copia, i):
            defineJogada(copia, computadorlet, i)
            if verificaVencedor(copia, computadorlet):
                return i

    
    for i in range(0, 23):
        copia = copiaTabuleiro(espaco)
        if temEspacoLivre(copia, i):
            defineJogada(copia, jogadorlet, i)
            if verificaVencedor(copia, jogadorlet):
                return i

    
    jogada = escolheJogadaAleatoriaDaLista(espaco, [0, 2, 20, 22])
    if jogada != None:
        return jogada

    
    if temEspacoLivre(espaco, 11):
            if jogada != None:
                    return 11
    if jogada != None:
        return escolheJogadaAleatoriaDaLista(espaco, [21, 10, 12, 1])

    

#Função que verifica se não há mais espaços livres, ou seja, deu velha	
def verificaVelha(tabuleiro):
    
    if tabuleiro[0] != ' ' and tabuleiro[1] != ' ' and tabuleiro[2] != ' ' and tabuleiro[10] != ' ' and tabuleiro[11] != ' ' and tabuleiro[12] != ' ' and tabuleiro[20] != ' ' and tabuleiro[21] != ' ' and tabuleiro[22] != ' ':
        
        return True
