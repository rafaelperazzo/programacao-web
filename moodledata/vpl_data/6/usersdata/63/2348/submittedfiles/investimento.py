# -*- coding: utf-8 -*-
from __future__ import division

a1=input('Digite o valor do investimento:')
taxa=input('taxa do crescimento percentual:')

a=a1+(taxa*a1)
b=a+(taxa*a)
c=b+(taxa*b)
d=c+(taxa*c)
e=d+(taxa*d)
f=e+(taxa*e)
g=f+(taxa*f)
h=g+(taxa*g)
i=h+(taxa*h)
j=i+(taxa*i)


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

