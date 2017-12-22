# -*- coding: utf-8 -*-

v=int(input('digite: '))
t=int(input('digite: '))
for i in range(0,t,1):
    ai=int(input('digite as trocas de volume: '))
    v=v+(ai)
    if v>=100:
        v=100
    elif v<=0:
        v=0
print(v)    