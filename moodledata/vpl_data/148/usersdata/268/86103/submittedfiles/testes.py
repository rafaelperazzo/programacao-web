# -*- coding: utf-8 -*-

n=int(input('Digite a : '))
soma=0
i=0
while(n>0):
    divisao=n%2
    soma= soma + divisao*10**i
    i=i+1
    n=n//2
print(soma)
    