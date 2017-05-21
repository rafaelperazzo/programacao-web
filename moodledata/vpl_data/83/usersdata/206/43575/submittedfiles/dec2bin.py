# -*- coding: utf-8 -*-

n=float(input('Digite o valor de n:'))
soma=0
i=0
while n>0:
    resto= n%10
    soma= soma+(2**i)*resto
    n=n//10
    i=i+1
print(soma)