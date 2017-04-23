# -*- coding: utf-8 -*-
n=int(input('digite um valor:'))
i=2
contador=0
while i<(n-1):
    if (n%i==0):
        contador=contador+1
        print('%d'%i)
    i=i+1
if (contador>0):
    print('NÃO PRIMO')
else:
    print('PRIMO!')
