# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
contador=0
soma=0
for i in range(2,n,1):
    if n%i==0:
        contador=contador+1
for i in range(1,n,1):
    if n%1==0:
        soma=soma+i
if soma==n:
    print('perfeito')
else:
    print('não é perfeito')

    

    