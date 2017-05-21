# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas ultilizaram a escada rolante: '))
tempo=0
for i in range(0,n,1):
    instante=int(input('Digite o instante em que esta pessoa passou pelo sensor: '))
    tempo=tempo+10
print(tempo)    