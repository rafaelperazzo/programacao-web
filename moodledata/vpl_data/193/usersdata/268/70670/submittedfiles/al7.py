# -*- coding: utf-8 -*-
n=int(input('Digite o número'))
i=1
SOMA=0

while (i<n):
    if (n%i)==0:
        print(i)
        SOMA= SOMA + i
    i= i+1

if (SOMA==n):
    print('PERFEITO')
else:
    print('NÃO PERFEITO')