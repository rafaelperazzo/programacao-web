# -*- coding: utf-8 -*-
n=int(input('digite o numero de competidores:'))
cont=0
for i in range(1,n+1,1):
    p1=int(input('digite a pontuacao  da primeira fase:'))
    p2=int(input('digite a pontuacao  da segunda fase:'))
    if p1+p2:
        cont=cont+1
pmin=int(input('digite a pontuacao minima:'))
print(cont)