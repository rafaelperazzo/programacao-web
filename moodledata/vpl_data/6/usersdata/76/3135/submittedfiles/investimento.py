# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

a1 = input('Digite o valor do investimento:')
t = input('Taxa do crescimento:')

a = a1 + (t*a1)
b = a + (t*a)
c = b + (t*b)
d = c + (t*c)
e = d + (t*d)
f = e + (t*e)
g = f + (t*f)
h = g + (t*g)
i = h + (t*h)
j = i + (t*i)

print('%.2f' %a)
print('%.2f' %b)
print('%.2f' %c)
print('%.2f' %d)
print('%.2f' %e)
print('%.2f' %f)
print('%.2f' %g)
print('%.2f' %h)
print('%.2f' %i)
print('%.2f' %j)