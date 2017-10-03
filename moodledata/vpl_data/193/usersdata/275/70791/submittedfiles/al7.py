# -*- coding: utf-8 -*-
i=1
soma=0
n= int(input('Digite o valor: '))
while (i<=n):
    if n%i==0:
        soma=i+i
        print(i)
    i=i+1
if (soma==n):
    print('PERFEITO')
else:
    ('NÃO PERFEITO')

