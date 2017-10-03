# -*- coding: utf-8 -*-

soma=0
n= int(input('Digite o valor de n: '))
i=1
while (i<n):
    if (n%i)==0:
        soma=soma+i
    
    i=i+1

if (soma==n):
    print('PERFEITO')
    
    