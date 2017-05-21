# -*- coding: utf-8 -*-
n=int(input('Digite um número binário: '))
soma=0
while (n>0):
    r=n%10
    soma=soma+(r*(2**i))
    i=i+1
    n=n//10
print(soma)   

