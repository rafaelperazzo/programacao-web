# -*- coding: utf-8 -*
N=int(input('Informe o número de competidores:'))
P=int(input('Informe o número mínimo de pontos:'))
competidores=0
for i in range(1,N+1,1):
    x=int(input('Informe a nota na primeira fase:'))
    y=int(input('Informe a nota na segunda fase:'))
    if (x+y) >= P:
        competidores=compatidores+1
print(competidores)        