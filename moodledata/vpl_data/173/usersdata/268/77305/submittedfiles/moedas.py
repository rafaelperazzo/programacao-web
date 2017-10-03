# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))

if(a>=b):
    while(c>a):
        divisao0= c//a
        c=c%a
    while(c>=b):
        divisao1 = c/b
        c=c%b
    if (c==0):
        print(divisao0)
        print(divisao1)
    else:
        print('N')
if(a<b):
    while(c>b):
        divisao0= c//b
        c=c%b
    while(c>=a):
        divisao1 = c/a
        c=c%a
    if (c==0):
        print(divisao1)
        print(divisao0)
    else:
        print('N')
if (a>b>c) or (b>a>c):
    print('N')