# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
soma=0
for i in range (1,n,1):
    if (n%i==0):
        print(i)
        soma=soma+1
if soma==n:
    print('Perfeito')
else:
    print('Não Perfeito')