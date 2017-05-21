# -*- coding: utf-8 -*-
n=int(input('Digite um número: '))
soma=0
i=0
while (n>0):
    r=n%2
    soma=soma+((10**i)*r)
    n=n//2
    i=i+1
print(soma)    


