# -*- coding: utf-8 -*-
N=int(input('Quantas pessoas o sensor detectou:'))
T=int(input('Instante em que a primeira pessoa passou:'))
L=0
for i in range(2,N+1,1):
    t=int(input('Instante em que a pessoa passou:'))
    a=(t-T)
    if a>10:
        L==10
    else:
        L==a
    t=T
print(L)    
    
    