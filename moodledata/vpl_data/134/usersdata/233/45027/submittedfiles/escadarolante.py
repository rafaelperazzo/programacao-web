# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas ultilizaram a escada rolante: '))
tempo=0
cont=0
a=0
for i in range(1,n+1,1):
    instante=int(input('Digite o instante em que esta pessoa passou pelo sensor: '))
    if instante==0:
        tempo=tempo+10
    elif instante>0:
        tempo=tempo+10+(instante-a)
    a=instante    
print(tempo)    