# -*- coding: utf-8 -*-
a=int(input('Valor de a:'))
b=int(input('Valor de b:'))
c=int(input('Valor de c:'))
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
    else:
        print(i)
        print('0')
        break
    i=i-1        
        
    

