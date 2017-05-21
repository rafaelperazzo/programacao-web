# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
cont=1
if b<a:
    qb=c//b
    if (c%b)%a==0:
        qa=(c%b)/a
        print(qa)
        print(qb)
    elif (c%b)%a!=0:
        while qb>=0:
            for i in range(1,b+1,1):
                qb=(c//b)-i
                j=qb*b
                z=c-j
                qa=z/a
            cont=cont+1
            if (c%b)%a==0:
                break
        if cont==b+1:
            print('N')
        elif (c%b)%a==0:
            print(qa)
            print(qb)
if a<b:
    qa=c//a
    if (c%a)%b==0:
        qb=(c%a)/b
        print(qa)
        print(qb)
    elif (c%a)%b!=0:
        while qa>=0:
            for i in range(1,a+1,1):
                qb=(c//a)-i
                j=qb*a
                z=c-j
                qb=z/b
            cont=cont+1
            if (c%a)%b==0:
                break
        if cont==a+1:
            print('N')
        elif (c%a)%b==0:
            print(qa)
            print(qb)
            

        
        
    
