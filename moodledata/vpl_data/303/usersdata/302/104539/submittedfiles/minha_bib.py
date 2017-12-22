# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
import random
def primo(n):
    contador = 0
    for i in range(2,n,1):
        if n%i == 0:
            contador += 1
        break
    if contador == 0:
        return True
    else:
        return False
def tabuleiro():
    matriz = (['00 |','01 ','|02 '],['10 |','11 ','|12 '],['20 |','21 ','|22 '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')
def jogador():

	return 'você joga com X' if random.randint(1,2) == 1 else 'você joga com O'
def valida(p):
    matriz = ['00','01','02'],['10','11','12'],['20','21','22']
    while(True):
            if str(matriz[0][0]) == str(p):
                return print('Próxima jogada:')
            else:
                return print('Jogada inválida, jogue novamente: ')
                    
def jogada(p,j):
    if p == '00':
        matriz[0][0] = j
    elif p == '01':
        matriz[0][1] = j
    elif p == '02':
        matriz[0][2] = j
    elif p == '10':
        matriz[1][0] = j
    elif p == '11':
        matriz[1][1] = j
    elif p == '12':
        matriz[1][2] = j
    elif p == '20':
        matriz[2][0] = j
    elif p == '21':
        matriz[2][1] = j
    elif p == '22':
        matriz[2][2] = j
def vitoria(j):
    vetor = ['']
    vencedor = ('')
    vetor = str(vetor)
    if j == 9:
        vencedor = 'VELHA'
        #Horizontais
    vetor[0] = matriz[0][0] + matriz[0][1] + matriz[0][2]
    vetor[1] = matriz[1][0] + matriz[1][1] + matriz[1][2]
    vetor[2] = matriz[2][0] + matriz[2][1] + matriz[2][2]
        #Verticais
    vetor[3] = matriz[0][0] + matriz[1][0] + matriz[2][0]
    vetor[4] = matriz[0][1] + matriz[1][1] + matriz[2][1]
    vetor[5] = matriz[0][2] + matriz[1][2] + matriz[2][2]
        #Diagonais
    vetor[6] = matriz[0][0] + matriz[1][1] + matriz[2][2]
    vetor[7] = matriz[0][2] + matriz[1][1] + matriz[2][0]  
    for i in range(len(vetor)):
        if vetor[i] == 'XXX':
            vencedor = 'jogador 1'
        else:
            vencedor = 'jogador 2'
    return vencedor