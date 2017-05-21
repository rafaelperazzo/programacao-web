# -*- coding: utf-8 -*-
N=int(input('Quantas pessoas o sensor detectou:'))
T=int(input('Instante em que a primeira pessoa passou:'))
contador=10
x=T
for i in range(2,N+1,1):
    t=int(input('Instante em que a pessoa passou:'))
    a=(t-T)
    contador=contador+a
    a=t
print(contador)    
    
    