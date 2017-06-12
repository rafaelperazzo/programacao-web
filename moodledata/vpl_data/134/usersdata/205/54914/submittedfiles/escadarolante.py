# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
tempo=0
for i in range(1,1+n,1):
    t=int(input('digite o instante que a i-ésima pessoa passou pelo sensor:'))
    if(i==1):
        t1=t
    elif(i==n):
        t2=t
tempo=t2-t1+10
print(tempo)