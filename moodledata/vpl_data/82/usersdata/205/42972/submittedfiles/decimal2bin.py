# -*- coding: utf-8 -*-
n=float(input('digite o valor de n:')
soma=0
i=0
while (n>0):
    resto=n%10
    soma=soma+resto*(2**i)
    i=i+1
    n=n//10
print(soma)
