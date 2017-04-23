# -*- coding: utf-8 -*-
n=int(input('digite um numero:'))
i=1
soma=0
contador=0
while i<(n-1):
    if (n%i==0):
        soma=soma+i
        contador=contador+1
        print('%d'%i)
    i=i+1
if soma:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')
    

