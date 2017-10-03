# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))

if(a>=b):
    qa= c//a
    c=c%a
    qb=c/b
    c=c%b
    if(c==0):
        print(qa)
        print(qb)
    else:
        print('N')
if(b>a)
    qb=c//b
    c=c%b
    qa=c/a
    c=c%a
    if(c==0):
        print(qa)
        print(qb)
    else:
        print('N')