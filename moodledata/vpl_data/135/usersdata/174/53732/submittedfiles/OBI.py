# -*- coding: utf-8 -*-
n=int(input('Número de competidores:'))
p=int(input('Número mínimo de pontos para ser convidado:'))
pontos=0
cont=0
for i in range(1,n+1,1):
    x=int(input('Número de pontos da primeira fase:'))
    y=int(input('Número de pontos da segunda fase:'))
    pontos=x+y
    if pontos>=p:
        cont=cont+1
print (cont)