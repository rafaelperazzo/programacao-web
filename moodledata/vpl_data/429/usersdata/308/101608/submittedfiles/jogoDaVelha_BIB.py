# -*- coding: utf-8 -*-
from random import randint
import copy
jogadasValidas = ['1 1', '0 0', '2 2', '0 2', '2 0', '0 1', '1 0', '2 1', '1 2']
def verificaVencedor(tabela): #Verifica se há vencedor || Parâmetro: Recebe a tabela para verificar || Retorno: Retorna o simbolo do vencedor
    for a in range(0, 3):
            if tabela[0][a]==tabela[1][a]==tabela[2][a]:
                return tabela[1][a]
            if tabela[a][0]==tabela[a][1]==tabela[a][2]:
                return tabela[a][0]
    if (tabela[0][0]==tabela[1][1]==tabela[2][2]) or (tabela[2][0]==tabela[1][1]==tabela[0][2]):
        return tabela[1][1]
    return ' '
def verificaIgualdade(valora, valorb ): #Verifica se sao iguais e retorna falso ou verdadeiro
    if valora==valorb:
        return True
    else: 
        return False
def solicitaNomeDoJogador(): #Solicita nome || Retorno: Nome do usuário
    nome=str(input('Qual o seu nome (ou apelido)? '))
    return nome
def solicitaSimboloDoHumano(): #Solicita simbolo || Retorno: Array = [Simbolo do humano, simbolo do computador]
    simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    while simbolo not in ('X','O'):
        simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    if simbolo== 'X':
        scomputador='O'
    else:
        scomputador='X'
    return [simbolo, scomputador]
def sorteioPrimeiraJogada(nomes): #Sorteio || Parâmetro: Nome dos jogadores e tabela || Retorno: Retorna o resultado do sorteio (0 ou 1)
    resultado = randint(0, 1)
    print('Vencedor do sorteio para inicio do jogo: %s' % nomes[resultado][0])
    return resultado
def validaJogada(jogada, visual): #Valida jogada || Paraâmetro: Nome dos jogadores e tabela || Retorno: Verdadeiro ou falso
    try: 
        return not verificaIgualdade(visual[int(jogada[0])][int(jogada[2])],' ')
    except:
        return True
def jogadaHumana(nomes, tabela): #Jogada humana || Parâmetro: Nome dos jogadores e tabela || Retorno: Tabela modificada    
    jogada = input('Qual sua jogada, %s: ' % nomes[0][0])
    while validaJogada(jogada, tabela):
        print('OPS!!! Essa jogada não está disponível. Tente novamente!')
        jogada = input('Qual sua jogada, %s: ' % nomes[0][0])
    tabela[int(jogada[0])][int(jogada[2])] = nomes[0][1]
    return tabela
def mostraTabuleiro(visual): #Mostrar tabuleiro || Parâmetro: tabela para ser mostrada
    for i in range (0, 3):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))
def jogarNovamente(): #Pergunta se deseja jogar novamente || Retorno: Verdadeiro ou falso
    x = input('Deseja jogar novamente? (S ou N) ')
    return verificaIgualdade(str.upper(x), 'N') 
def jogadaComputador(nomes, tabela): #Jogada do computador || Parâmetro: Nome dos jogadores e tabela || Retorno: Tabela modificada 
    if tabela == [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']] or tabela == [[' ',' ', ' '], [' ',nomes[0][1],' '], [' ', ' ', ' ']]:
        lista = ['0 0', '0 2', '2 0', '2 2']
        jogada = lista[randint(0, 3)]
        tabela[int(jogada[0])][int(jogada[2])] = nomes[1][1]
        return tabela  
    for jogador in [nomes[1][1], nomes[0][1]]:    
        for jogada in jogadasValidas:
            if not validaJogada(jogada, tabela):
                    copia = copy.deepcopy(tabela)
                    copia[int(jogada[0])][int(jogada[2])] = jogador
                    vencedor = verificaVencedor(copia)
                    print('Testou %s com %s' % (jogada, jogador))
                    if vencedor == 'X' or vencedor == 'O':
                        tabela[int(jogada[0])][int(jogada[2])] = nomes[1][1]
                        return tabela
    for jogada in jogadasValidas:
        if not validaJogada(jogada, tabela):
            copia = copy.deepcopy(tabela)
            copia[int(jogada[0])][int(jogada[2])] = nomes[1][1]
                for jogada2 in jogadasValidas:
                        copia2 = copy.deepcopy(copia)
                        if not validaJogada(jogada2, copia2):
                            copia2[int(jogada2[0])][int(jogada2[2])] = nomes[1][1]
                            if verificaVencedor(copia2) == nomes[1][1]:
                                tabela[int(jogada[0])][int(jogada[2])] = nomes[1][1]
                                print('Jogada estratégica')
                                return tabela
    if not validaJogada('1 1', tabela):
        tabela[1][1] = nomes[1][1]
        return tabela
    jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    while validaJogada(jogada, tabela):
        jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    tabela[int(jogada[0])][int(jogada[2])] = nomes[1][1]
    return tabela