# -*- coding: utf-8 -*-


n=int(input('digite o valor de n: '))
exp=0
soma=0
while (n>0):
    resto=n%2
    soma=soma+(resto*(10**exp))
    exp=exp+1
    n=n//2
print(soma)