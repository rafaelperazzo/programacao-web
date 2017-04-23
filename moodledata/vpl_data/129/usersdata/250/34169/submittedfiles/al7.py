# -*- coding: utf-8 -*-
n=int(input('digite um numero:'))
i=1
contador=0
soma=0
while i<(n-1):
    if (n%i==0):
        contador=contador+1
        print('%d'%i)
    i=i+1
if contador>0:
    soma=soma+i
    print('PERFEITO')
else:
    print('NÃO PERFEITO')
    

