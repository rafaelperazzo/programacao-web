# -*- coding: utf-8 -*-
N=int(input('número de pessoas detectadas:'))
T=int(input('primeiro tempo:'))
contador=10
for i in range (2,N+1,1):
    t=int(input('tempo de funcionamento:'))
    x=t-T
    contador=contador+x
    T=t
print('contador')