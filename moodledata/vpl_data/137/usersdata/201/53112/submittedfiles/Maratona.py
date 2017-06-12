# -*- coding: utf-8 -*-
N=int(input('Número de postos de água:'))
M=int(input('Distância intermediaria máxima:'))
for i in range(1,N+1,1):
    n=int(input('Distância entre os postos:'))
    n=n-M
if n<=M:
    print('S')
else:
    print('N')