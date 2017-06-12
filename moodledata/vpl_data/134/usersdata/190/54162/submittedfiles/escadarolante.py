# -*- coding: utf-8 -*-
n=int(input('pessoas que usaram a escada:'))
t=int(input('instante em que usou:'))
tempo=10
cont=t
for i in range (1,n,1):
    t=int(input('instante em que usou:'))
    tempo=tempo+(t-cont)
    cont=t
print(tempo)