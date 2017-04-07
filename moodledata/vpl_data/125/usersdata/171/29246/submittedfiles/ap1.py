# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if  a<=b and a<=c:
    print('%d'%a)
    if b<=c:
        print('%d'%b)
        print('%d'%c)
    else:
        print('%d'%c)
