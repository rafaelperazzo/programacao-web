# -*- coding: utf-8 -*-
n=int(input('numero de competidores:'))
p=int(input('numero minimo de pontos:'))
cont=0
for i in range(1,n+1,1):
    x=int(input('pontuação na primeira etapa:'))
    y=int(input('pontuação na segunda etapa:'))
    pontuação=x+y
    if pontuação>=p:
        cont=cont+1
print(cont)