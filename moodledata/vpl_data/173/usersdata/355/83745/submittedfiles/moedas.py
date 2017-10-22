# -*- coding: utf-8 -*-
a=int(input('Digite o valor da moeda 1: '))
b=int(input('Digite o valor da moeda 2: '))
c=int(input('Digite o valor da cédula: '))

if a>b:
    if c%a==0:
        x=c/a     
        print(x)
        print(0)
    if c%b==0:
        x=c/b
        print(0)
        print(x)
    if c%a!=0:
        if c%b==0:
            x=c//a
            y=c%a
            z=y/b
            print(x)
            print(z)
        else:
            print('N')
if b>a:
    if c%a==0:
        x=c/a     
        print(x)
        print(0)
    if c%b==0:
        x=c/b
        print(0)
        print(x)
    if c%b!=0:
        if c%a==0:
            x=c//b
            y=c%b
            z=y/a
            print(z)
            print(x)
        if c%a!=0:
            x=c//a
            y=c%a
            if (y/b)==0:
                print(x)
                print(z)
            else:
                print('N')
            
            
        