# -*- coding: utf-8 -*-

A=int(input('quantidade de competidores:'))
B=int(input('quantidade de competidores:'))

cont=0
for i in range(1,A+1,1):
    c=int(input('quantidade de pontos da prova 1:'))
    d=int(input('quantidade de pontos da prova 2:'))
    if (c+d)>=B:
        cont=cont+1
print(cont)        
        