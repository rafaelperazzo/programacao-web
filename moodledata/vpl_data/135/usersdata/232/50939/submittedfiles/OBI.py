# -*- coding: utf-8 -*-
N=int(input('Digite o número de participantes: '))
P=int(input('Digite o total mínimo de pontos: '))
cont=0
for i in range (1,n+1,1):
    X=int(input('Digite a pontuação do participante na primeira fase: '))
    Y=int(input('Digite a pontuação do participante na segunda fase: '))
    if X+Y==P:
        cont=cont+1
print(cont)        