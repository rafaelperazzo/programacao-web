# -*- coding: utf-8 -*-
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
i=c//a
while i>0:
    x=c-(i*a)
    if x>=b:
        qp=x//b
        if x>=b:
            qb=x//b
            if x%b==0:
                print(i)
                print(qb)
            else:
                print('n')
        i=i-1