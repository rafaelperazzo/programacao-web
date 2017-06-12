# -*- coding: utf-8 -*-
n=int(input('digite o número de competidores:'))
p=int(input('dgite o numero máximo de pontos para o convite:'))
pontos=0
cont=0
for i in range(1,n+1,1):
    p1=int(input('digite o número de pontos obtidos na primeira fase:'))
    p2=int(input('digite o numero de pontos obtidos na segunda fase:'))
    pontos=p1+p2
    if (pontos>=p):
        cont=cont+1
print(cont)