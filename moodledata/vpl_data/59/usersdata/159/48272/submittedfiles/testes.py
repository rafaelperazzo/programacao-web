# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
i=c//a
while i>0:
    x=c-(i*a)
    if x>=b:
        qb=x//b
        if x%b==0:
            print(i)
            print(qb)
            break
        else:
            print('N')
            break
    i=i-1        
        