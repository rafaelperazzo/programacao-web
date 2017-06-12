# -*- coding: utf-8 -*-
N=int(input('digite o número de pessoas detectadas:'))
v=int(input('digite o primeiro tempo:'))
contador=10
for i in range (2,N+1,1):
    t=int(input('tempo de funcionamento:'))
    x=t-v
    contador=contador+x
    v=t
print('contador')