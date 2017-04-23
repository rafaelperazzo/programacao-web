# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

i= float(input('digite o valor do investimento:'))
t= float(input('digite a taxa de crecimento anual em numero decimal:'))

a1=i+t*i
a2=a1+t*a1
a3=a2+t*a2
a4=a3+t*a3
a5=a4+t*a4
a6=a5+t*a5
a7=a6+t*a6
a8=a7+t*a7
a9=a8+t*a8
a10=a9+t*a9

print('%.2f' %a1)
print('%.2f' %a2)
print('%.2f' %a3)
print('%.2f' %a4)
print('%.2f' %a5)
print('%.2f' %a6)
print('%.2f' %a7)
print('%.2f' %a8)
print('%.2f' %a9)
print('%.2f' %a10)