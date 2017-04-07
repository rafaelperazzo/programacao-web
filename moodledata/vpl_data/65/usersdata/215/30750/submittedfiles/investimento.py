# -*- coding: utf-8 -*-
from __future__ import division
a1=float(input('digite o capital inicial:'))
a2=float(input('digite a taxa de crescimento anual:'))
i=a2/100
m1=a1*(1+i)
m2=m1*(1+i)
m3=m2*(1+i)
m4=m3*(1+i)
m5=m4*(1+i)
m6=m5*(1+i)
m7=m6*(1+i)
m8=m7*(1+i)
m9=m8*(1+i)
m10=m9*(1+i)
m11=a1*((1+i))**10

print('%.2f'%m1)
print('%.2f'%m2)
print('%.2f'%m3)
print('%.2f'%m4)
print('%.2f'%m5)
print('%.2f'%m6)
print('%.2f'%m7)
print('%.2f'%m8)
print('%.2f'%m9)
print('%.2f'%m10)