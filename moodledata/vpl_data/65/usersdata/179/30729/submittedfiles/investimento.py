# -*- coding: utf-8 -*-
from __future__ import division

v1=float9input('digite o valor do investimento:'))
tx=float(input('digite o valor da taxa de crescimento por ano:'))
i=tx/100
iv1=v1*(1+i)
iv2=iv1*(1+i)
iv3=iv2*(1+i)
iv4=iv3*(1+i)
iv5=iv4*(1+i)
iv6=iv5*(1+i)
iv7=iv6*(1+i)
iv8=iv7*(1+i)
iv9=iv8*(1+i)
iv10=iv9*(1+i)
iv11=v1*((1+i))**10
print('%.2f'%iv1)
print('%.2f'%iv2)
print('%.2f'%iv3)
print('%.2f'%iv4)
print('%.2f'%iv5)
print('%.2f'%iv6)
print('%.2f'%iv7)
print('%.2f'%iv8)
print('%.2f'%iv9)
print('%.2f'%iv10)