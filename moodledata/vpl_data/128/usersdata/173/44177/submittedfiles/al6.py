# -*- coding: utf-8 -*-
n=int(input('Digite um número: '))
for i in range(2,n,1):
    if(n%i==0):
        print(i)
        print('NÃO PRIMO')
    else:
        print('PRIMO')