# -*- coding: utf-8 -*-
from __future__ import division

iv=input('digite o valor do investimento:')
tx=input('digite o valor da taxa:')

tx=0.045
a1=iv+(tx*iv)
a2=a1+(tx*a1)
a3=a2+(tx*a2)
a4=a3+(tx*a3)
a5=a4+(tx*a4)
a6=a5+(tx*a5)
a7=a6+(tx*a6)
a8=a7+(tx*a7)
a9=a8+(tx*a8)
a10=a9+(tx*a9)

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

