# -*- coding: utf-8 -*-
a=int(input('Digite o valor da moeda 1: '))
b=int(input('Digite o valor da moeda 2: '))
c=int(input('Digite o valor da cédula: '))

if a>b:
    if c%a==0:
        x=c/a     
        print(x)
        print(0)
    else:
        x=c//a