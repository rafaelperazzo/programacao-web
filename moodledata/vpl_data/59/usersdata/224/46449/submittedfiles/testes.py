# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
soma=0
i=2
while i<n:
    if n%i==0:
        soma=soma+i
    i=i+1
if soma==n:
    print('perfeito')
else:
    print('n é perfeito' )