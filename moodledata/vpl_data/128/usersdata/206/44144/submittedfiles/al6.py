# -*- coding: utf-8 -*-

n= int(input('Digite um numero:'))
cont=0
for i in range(2,n,1):
    n= n//2
    if n%i==0:
        print(n)
