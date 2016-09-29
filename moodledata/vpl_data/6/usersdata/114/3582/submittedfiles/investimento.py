# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

n=input('Valor do investimento: ')
taxa=input('Taxa de crescimento percentual: ')

x1=n + (taxa*n)
x2=x1 + (taxa*x1)
x3=x2 + (taxa*x2)
x4=x3 + (taxa*x3)
x5=x4 + (taxa*x4)
x6=x5 + (taxa*x5)
x7=x6 + (taxa*x6)
x8=x7 + (taxa*x7)
x9=x8 + (taxa*x8)
x10=x9 + (taxa*x9)

print ('%.2f' % x1)
print ('%.2f' % x2)
print ('%.2f' % x3)
print ('%.2f' % x4)
print ('%.2f' % x5)
print ('%.2f' % x6)
print ('%.2f' % x7)
print ('%.2f' % x8)
print ('%.2f' % x9)
print ('%.2f' % x10)