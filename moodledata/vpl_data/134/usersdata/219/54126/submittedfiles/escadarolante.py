# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas que passaram na escada: '))
soma=0
for i in range (1,n+1,1):
    t=int(input('digite o tempo: '))
    soma=soma+t
if soma%10==0:
    print(soma)