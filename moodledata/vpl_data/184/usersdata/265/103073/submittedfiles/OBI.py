# -*- coding: utf-8 -*-
N=int(input('digite a quantidade de participantes: '))
P=int(input('digite a pontuação miníma: '))
cont=0
for i in range (0,N,1):
    X=int(input('digite a primeira pontuação:'))
    Y=int(input('digite a segunda pontuaçao: '))
    if (X+Y)>=P:
        cont=cont+1
print(cont)