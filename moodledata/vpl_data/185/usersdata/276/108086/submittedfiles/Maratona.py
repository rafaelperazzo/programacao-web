# -*- coding: utf-8 -*-

N = int (input ('Digite a quantidade de postos de agua: '))
M = int (input ('Digite a distancia intermediaria do jogador: '))

a = []

x = 0
cont = 0

for i in range (0,N,1):
    distancia = int (input('Digite a distancia do posto: '))
    if distancia - x <= M  or distancia == 0:
        cont = cont + 1
        x = distancia

if cont == N:
    print ('S')
else:
    print ('N')
