# -*- coding: utf-8 -*-
a=int(input('Digite a :'))
soma=0
for i in range (1,a,1):
    if a%i==0:
        soma=soma+i
        print(i)
if soma==a:
    print('PERFEITO')
    
else:
    print('NÃO PERFEITO')
