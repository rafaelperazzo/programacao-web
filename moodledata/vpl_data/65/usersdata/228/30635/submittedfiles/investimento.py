# -*- coding: utf-8 -*-
from __future__ import division

a=float(input('digite um valor para o investimento:'))
b=float(input('digite um em porcentagem para a taxa de crescimento:'))
c=a+(a*b)
print('%.2f'%c)
d=c+(c*b)
print('%.2f'%d)
e=d+(d*b)
print('%.2f'%e)
f=e+(e*b)
print('%.2f'%f)
