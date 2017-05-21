# -*- coding: utf-8 -*-

n=int(input('Digite o número binário:'))
soma=0
i=0
while n>0:
    resto=n%10
    soma=soma+resto*(2**i)
    n=n//10
    i=i+1
print(soma)