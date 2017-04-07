# -*- coding: utf-8 -*-
from __future__ import division

n1=float(input('digite o valor inicial do seu investimento:'))
n2=float(input('digite o valor da taxa de crescimento anual:'))
i=n2/100
m1=n1*(1+i)
m2=m1*(1+i)
m3=m2*(1+i)
m4=m3*(1+i)
m5=m4*(1+i)
m6=m5*(1+i)
m7=m6*(1+i)
m8=m7*(1+i)
m9=m8*(1+i)
m10=m9*(1+i)

m11=n1*((1+i))**10

print('mês 1:------->%.2f'%m1)
print('mês 2:------->%.2f'%m2)
print('mês 3:------->%.2f'%m3)
print('mês 4:------->%.2f'%m4)
print('mês 5:------->%.2f'%m5)
print('mês 6:------->%.2f'%m6)
print('mês 7:------->%.2f'%m7)
print('mês 8:------->%.2f'%m8)
print('mês 9:------->%.2f'%m9)
print('mês 10:------->%.2f'%m10)


print('volte sempre')

