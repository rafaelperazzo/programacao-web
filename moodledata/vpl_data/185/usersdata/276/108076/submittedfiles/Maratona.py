# -*- coding: utf-8 -*-

N = int (input ('Digite a quantidade de postos de agua: '))
M = int (input ('Digite a distancia intermediaria do jogador: '))

a = []

for i in range (0,N,1):
    distancia = int (input('Digite a distancia do posto: '))
    a.append (distancia)
    
x = 0
cont = 0
while (i<=N):
    if a[i] - x <= M  or a[i] == 0:
        cont = cont + 1
        x = a[i]
    else:
        break

if cont == N:
    print ('S')
else:
    print ('N')
