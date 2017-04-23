# -*- coding: utf-8 -*-
x=int(input('digite o valor:'))
soma=0
for i in range(1,x,1):
    if x%i==0:
        soma=soma+1
if soma==n:
    print('perfeito')
else:
    print('não perfeito')