# -*- coding: utf-8 -*-
n=float(input('digite o número de pessoas que passaram pela escada:'))
cont=1
while cont<=n:
    t=int(input('digite o tempo a qual a pessoa passou pela escada:'))
    if cont==1:
        ti=t
    if cont==n:
        T=t+10-ti
    cont=cont+1
print(T)