# -*- coding: utf-8 -*-
n=int(input('Digite o número de competidores:'))
p=int(input('Digitar o número mínimo de pontos:'))
cont=0
for i in range (1,n+1,1):
    x=int(input('Pontos na primeira fase:'))
    y=int(input('Pontos na segunda fase:'))
    soma=x+y
    if soma>=p:
        cont=cont+1
print(cont)