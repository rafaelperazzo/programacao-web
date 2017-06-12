# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas dectectadas pelo sensor: '))
i=0
for i in range(1,n+1,1):
    t=int(input('Digite instate da i-ésima pessoa que passou pelo sensor: '))
    if(i==1):
        t1=t
    elif(i==n):
        t2=t
tempo=t2-t1+10
print(tempo)