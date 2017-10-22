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
    if c%b==0:
        x=c/b
        print(0)
        print(x)
    else:
        x=c//b
        y=c%b
        if y==0:
            z=y/a
            print(z)
            print(x)
        else: 
            print('N')