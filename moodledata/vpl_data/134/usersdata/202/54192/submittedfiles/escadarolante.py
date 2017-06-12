# -*- coding: utf-8 -*-
N=int(input('digite o valor de N:'))
cont=1
while cont<=N:
    T=int(input('digite o valor de T:'))
    if cont==1:
        T1=T
    if cont==N:
        tempo=(T+10)-T1
    cont=cont+1
print(tempo)    