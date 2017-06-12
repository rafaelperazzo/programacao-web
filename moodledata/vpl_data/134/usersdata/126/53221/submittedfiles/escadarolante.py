# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas que passaram pelo sensor:'))
m=0
t=0
i=0
soma=0
p=m
if n>0:
    for i in range(1,n+1,1):
        m=int(input('digite o instante em que a pessoa passou pelo sensor:'))
        t=(m-p)
        p=m
        i=i+1
        soma=soma+t
    soma=soma+10
print(soma)