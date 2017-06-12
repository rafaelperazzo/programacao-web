# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas que passaram pelo sensor:'))
a=[]
m=0
if n>0:
    for i in range(1,n+1,1):
        m=int(input('digite o instante em que a pessoa passou pelo sensor:'))
        a.append(m)
        i=i+1

