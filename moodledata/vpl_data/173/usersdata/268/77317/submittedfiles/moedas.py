# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))

if(a>=b):
    while(c>=a):
        qa= c//a
        c=c%a
    while(c>=b):
        qb = c/b
        c=c%b
    if (c==0):
        print(qa)
        print(qb)
    else:
        print('N')
else:
    while(c>=b):
        qb= c//b
        c=c%b
    while(c>=a):
        qa = c/a
        c=c%a
    if (c==0):
        print(qa)
        print(qb)
    else:
        print('N')
