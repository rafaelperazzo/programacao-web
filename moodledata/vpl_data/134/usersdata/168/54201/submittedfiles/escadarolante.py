# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas que o senso detectou: '))
i=0
for i in range (1,n+1,1):
    t=int(input('Digite o instante que a i-ésima pessoa passou pelo sensor: '))
    if (i--1):
        t1=t
    elif (i==n):
        t2=t
tempo=t2-t1+10
print(tempo)