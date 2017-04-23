# -*- coding: utf-8 -*-
n=int(input('Digite o valor d n:'))
SOMA=0
for i in range (1,n,1):
    if n%i==0:
        SOMA=SOMA+i
if SOMA==n:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')