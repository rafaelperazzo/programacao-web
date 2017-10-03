# -*- coding: utf-8 -*-
n=int(input('Digite n : '))
i=0
soma=0
while(n>0):
    divisao= n%2
    soma= soma + divisao*10**i
    n=n//10
    i=i+1
print(soma)
