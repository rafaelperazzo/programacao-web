# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas :'))
for i in range(1,n+1,1):
    t=int(input('digite o tempo :'))
    if i==1:
        t1=t
    if i==n:
        t2=t
tempo=t2-t1+10        
print(tempo)        