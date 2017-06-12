# -*- coding: utf-8 -*-
n=int(input('Digite o Numero de pessoas: '))
i=0
for i in range(1,n+1,1):
    t=int(input('Digite o instante que pessoa passa pelo sensor: '))
    if (i==1):
        t1=t
    elif (i==n):
        t2=t
tempo=t2-t1-10
print(tempo)