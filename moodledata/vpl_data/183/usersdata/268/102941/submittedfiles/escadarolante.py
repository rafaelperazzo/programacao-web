# -*- coding: utf-8 -*-
N=int(input('pessoas: '))
soma=0

for i in range(0,N,1):
    T=int(input('instante'))
    if i==0:
        primeiro=T
    if i==(N-1):
        ultimo=T
resposta= ultimo + 10 - primeiro
print(resposta)