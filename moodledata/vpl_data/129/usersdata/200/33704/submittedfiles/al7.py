# -*- coding: utf-8 -*-
n=int(input('digite um numero:'))
i=0
for cont in range(1,n,1):
    if n%cont==0:
        print(cont)
        i=i+cont
if i==n:
    print('perfeito')
else:
    print('NAO PERFEITO')