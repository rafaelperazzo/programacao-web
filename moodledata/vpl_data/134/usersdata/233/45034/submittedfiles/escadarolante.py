# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas ultilizaram a escada rolante: '))
instante=int(input('Digite o instante em que esta pessoa passou pelo sensor: '))
if n>0:
    tempo=10
cont=instante
for i in range(1,n,1):
    instante=int(input('Digite o instante em que esta pessoa passou pelo sensor: '))
    tempo=tempo+10+(instante-cont)
    cont=instante
print(tempo)    