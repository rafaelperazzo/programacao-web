# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=(b*b)-(4*a*c)
if d >= 0:
    x1=(-b+(d**1/2))/2*a
    x2=(-b-(d**1/2))/2*a
    print('%.2f'%x1)
    print('%.2f'%x2)
else:
        print('srr')


    