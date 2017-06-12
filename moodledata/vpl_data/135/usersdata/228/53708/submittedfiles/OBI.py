# -*- coding: utf-8 -*-
n=int(input('digite o numero de participantes:'))
ponts=int(input('digite o numero de pontos para a seleção'))
cont=0
for i in range(1,n+1,1):
    x=int(input('digite os pontos da primeira fase:'))
    y=int(input('digite os pontos da segunda fase:'))
    if (x+y)>=p:
        cont=cont+1
print(cont)        




