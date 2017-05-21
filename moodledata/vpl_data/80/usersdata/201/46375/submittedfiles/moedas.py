# -*- coding: utf-8 -*-
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
i=c//a
while a>0:
    x=c-(i*a)
    if x>=b:
        qb=x//b
        if x%b==0:
            print(i)
            print(qb)
        else:
            print('N')
    i=i-1
