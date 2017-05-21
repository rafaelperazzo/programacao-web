# -*- coding: utf-8 -*-
n=int(input('Número de pessoas:'))
contador=0
a=0
for i in range (1,n+1,1):
    t=int(input('Instante em que passou:')
    b=t-a
    a=t
    contador=contador+b
print(contador)    