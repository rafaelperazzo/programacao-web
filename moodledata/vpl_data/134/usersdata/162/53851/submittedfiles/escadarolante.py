# -*- coding: utf-8 -*-
N=int(input('Digite o número de pessoas detectadas:'))
v=int(input('Digite o primeiro tempo:'))
cont=10
for i in range(2,N+1,1):
    t=int(input('Digite o tempo de funcionamento:'))
    x=t-v
    cont=cont+x
    v=t
print(cont)    