# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

def simbolo():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Isira um símbolo válido')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    return

def sorteio(tipo):
sorteado = -1
while(True) :
    sorteado = random.randint(0,num_grupos-1)
    if (tipo=='G') :
        if (grupos_sorteados[sorteado] == -1):
            break
    else:
        if (datas_sorteadas[sorteado] == -1):
            break
    return sorteado

for i in range (num_grupos+1,1):
    input(' Pressione ENTER para sortear o %dº grupo...' % i)
    indice_grupo = sorteio('G')
    mostra_sorteado('G',indice_grupo)
    input(' Pressione ENTER para sortear a %dª data...' % i)
    indice_data = sorteio('D')
    time.sleep(3)
    mostra_sorteado('D',indice_data)
    salva_sorteio(indice_grupo, indice_data)
print(' ------------------------------------------------- ')
print('           Ordem de apresentação do P1 ')
print(' ------------------------------------------------- ')
print(' DIA 1: ')
print(' ------------------------------------------------- ')










inicio = ['computador','nome']
inicio_sorteio = [1,1]
num_inicio = len(inicio)

def sorteio (x):
    sorteado = 1
    if sorteado in inicio_sorteio:
        return inicio_sorteio.index

