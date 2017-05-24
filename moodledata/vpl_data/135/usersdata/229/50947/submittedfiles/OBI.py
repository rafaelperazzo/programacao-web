# -*- coding: utf-8 -*-

comp1=int(input('digite a quantidade de competidores:'))
comp2=int(input('digite a quantidade de competidores:'))

cont=0

for i in range(1,comp1+1,1):
    p1=int(input('digite a quantidade de pontos da 1 prova:'))
    p2=int(input('digite a quantidade de pontos da 2 prova:'))
    
    if (p1+p2)>=comp2:
        cont=cont+1
print(cont)