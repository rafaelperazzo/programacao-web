# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas ultilizaram a escada rolante: '))
instante=int(input('Digite o instante em que esta pessoa passou pelo sensor: '))
tempo=0
cont=instante
for i in range(1,n,1):
    instante2=int(input('Digite o instante em que esta pessoa passou pelo sensor: '))
    tempo=tempo+10+(instante-cont)
    cont=instante2
print(tempo)    