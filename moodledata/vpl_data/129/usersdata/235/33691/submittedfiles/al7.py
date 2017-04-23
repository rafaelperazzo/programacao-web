# -*- coding: utf-8 -*-
x=int(input('digite o valor:'))
soma=0
for i in range(1,x,1):
    if x%i==0:
        print(i)
        soma=soma+i
if soma==x:
    print('perfeito')
else:
    print('NÃO PERFEITO')