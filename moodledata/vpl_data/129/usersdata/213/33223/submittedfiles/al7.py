# -*- coding: utf-8 -*-
n=int(input('Informe um número: '))
somaDivisores=0
for i in range(1,n,1):
    if n%i==0:
        somaDivisores=somaDivisores+1

if soma==n:
    print('PERFEITO')
else:
    print('NÃO É PERFEITO')