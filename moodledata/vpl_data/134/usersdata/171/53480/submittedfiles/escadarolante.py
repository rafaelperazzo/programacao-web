# -*- coding: utf-8 -*-
n=int(input('digite numero de pessoas:'))
x=int(input('instante em que a pessoa passou:'))
a=x
contador=10
for i in range(2,n+1,1):
    t=int(input('instante em que a pessoa passou:'))
    b=(t-a)
    contador=contador+b
    a=t
print(contador)