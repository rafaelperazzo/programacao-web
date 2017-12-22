# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

def simbolo():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Isira um símbolo válido')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    return

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

for i in range (num_grupos+1,1)
   74     input(' Pressione ENTER para sortear o %dº grupo...' % i)
   75     indice_grupo = sorteio('G')
   76     time.sleep(2)
   77     mostra_sorteado('G',indice_grupo)
   78     input(' Pressione ENTER para sortear a %dª data...' % i)
   79     indice_data = sorteio('D')
   80     time.sleep(3)
   81     mostra_sorteado('D',indice_data)
   82     salva_sorteio(indice_grupo, indice_data)
   83 time.sleep(2)
   84 print(' ------------------------------------------------- ')
   85 print('           Ordem de apresentação do P1 ')
   86 print(' ------------------------------------------------- ')
   87 print(' DIA 1: ')
   88 print(' ------------------------------------------------- ')










inicio = ['computador','nome']
inicio_sorteio = [1,1]
num_inicio = len(inicio)

def sorteio (x):
    sorteado = 1
    if sorteado in inicio_sorteio:
        return inicio_sorteio.index

