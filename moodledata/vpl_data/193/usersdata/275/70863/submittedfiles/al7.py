# -*- coding: utf-8 -*-
i=1
soma=0
n= int(input('Digite o valor: '))
while (i<n):
    if n%i==0:
        soma=soma+i
        print(i)
    i=i+1
if (soma+1==n):
    print('PERFEITO')
else:
    ('NÃO PERFEITO')

