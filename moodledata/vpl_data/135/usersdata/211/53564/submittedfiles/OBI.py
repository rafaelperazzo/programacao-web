# -*- coding: utf-8 -*-
A=int(input('quantidade de competidores:'))
B=int(input('quantidade de competidores:'))
cont=0
for i in range(1,A+1,1):
    C=int(input('quantidades de pontos prova 1:'))
    D=int(input('quantidades de pontos prova 2:'))
    if (C+D)>=B:
        cont=cont+1
print(cont)