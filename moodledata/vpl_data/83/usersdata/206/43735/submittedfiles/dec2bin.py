# -*- coding: utf-8 -*-

n=int(input('Digite o valor de n:'))
soma=0
i=0
while n>0:
    resto= n%2
    soma= soma+(10**i)*resto
    n=n//2
    i=i+1
print(soma)