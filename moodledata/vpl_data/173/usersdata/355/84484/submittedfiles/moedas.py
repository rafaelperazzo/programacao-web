# -*- coding: utf-8 -*-
a=int(input('Digite o valor da moeda 1: '))
b=int(input('Digite o valor da moeda 2: '))
c=int(input('Digite o valor da cédula: '))

if c%a==0:
    x=c/a
    y=c/b
    if c%b==0:
        print(x)
        print('0')
        print('0')
        print(y)
    else:
        print(x)
        print('0')
        z=c%b
        v=z/a
        print(c//b)
        print(v)
if c%a!=0:
    if c%b==0:
        z=c%a
        x=z/b
        print(c//a)
        print(x)
        print('0')
        print(c/b)
    else:
        z=c%a
        x=z/b
        if (z%b)==0:
            print(c//a)
            print(x)
        else: 
            print('N')
            
        