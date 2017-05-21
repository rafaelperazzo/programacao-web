# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas: '))
Ti=int(input('Digite o instante T da primeira pessoa: '))
contador=10
for i in range (2,n+1,1):
    T=int(input('Digite o instante T em que a pessoa passou pelo sensor: '))
    TF=T-Ti
    contador=contador+TF
    Ti=T
print(contador)