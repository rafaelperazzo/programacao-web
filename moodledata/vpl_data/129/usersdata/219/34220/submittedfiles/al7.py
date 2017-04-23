# -*- coding: utf-8 -*-
a=int(input('Digite a :'))
soma=0
for i in range (1,a,1):
    if n%i==0:
        soma=soma++1
        print(i)
if soma==n:
    print('PERFEITO')
    
else:
    print('NÃO PERFEITO')
