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
        y=c%a
        z=y/b
        print(x)
        print(z)
else:
    if c%b==:
        x=c/b
        print(x)
        print(0)
    else:
        x=c//b
        y=c%b
        z=y/a
        print(z)
        print(x)
    