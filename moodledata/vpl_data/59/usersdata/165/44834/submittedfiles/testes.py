# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite um numero:'))

for n in range(1000,10000,1):
    a=n//100
    b=n%100
    if n**(1/2)==a+b:
        print(n)