# -*- coding: utf-8 -*-

p=int(input('digite o  número de pontos:'))
d=int(input('digite a distância determinada máxima:'))
i=0
cont=0
at=0
for i in range(1,p,1):
    prox=int(input('digite a entrada:'))
    if prox-at>d:
        cont=cont+1
        at==prox
        print('N')
    else:
        print('S')